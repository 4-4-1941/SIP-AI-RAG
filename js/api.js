(() => {
  "use strict";

  const cfg = window.SIP_CONFIG;

  function url(path) {
    return `${cfg.API_BASE_URL}${path}`;
  }

  async function request(path, options = {}) {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), cfg.REQUEST_TIMEOUT_MS);

    try {
      const response = await fetch(url(path), {
        ...options,
        headers: {
          "Content-Type": "application/json",
          ...(options.headers || {})
        },
        signal: controller.signal
      });

      let data = null;
      try {
        data = await response.json();
      } catch (_) {
        data = null;
      }

      if (!response.ok) {
        const detail = data?.detail || `HTTP ${response.status}`;
        throw new Error(detail);
      }

      return data;
    } catch (error) {
      if (error.name === "AbortError") {
        throw new Error("La consulta excedió el tiempo de espera.");
      }
      throw error;
    } finally {
      clearTimeout(timeout);
    }
  }

  window.SIP_API = Object.freeze({
    health() {
      return request(cfg.HEALTH_ENDPOINT, { method: "GET" });
    },

    chat(message) {
      return request(cfg.CHAT_ENDPOINT, {
        method: "POST",
        body: JSON.stringify({ message })
      });
    }
  });
})();
