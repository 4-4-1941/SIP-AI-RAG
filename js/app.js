(() => {
  "use strict";

  const cfg = window.SIP_CONFIG;
  const api = window.SIP_API;

  function byId(id) {
    return document.getElementById(id);
  }

  function setText(element, text) {
    if (element) element.textContent = text;
  }

  function init() {
    const input = byId("q") || byId("queryInput");
    const button = byId("send") || document.querySelector('#queryForm button[type="submit"]');
    const form = byId("queryForm");
    const output = byId("out");
    const charCount = byId("charCount");

    if (!input) return;

    input.maxLength = cfg.MAX_QUERY_LENGTH;

    function updateCount() {
      if (charCount) {
        setText(charCount, `${input.value.length} / ${cfg.MAX_QUERY_LENGTH}`);
      }
    }

    async function submit(event) {
      if (event) event.preventDefault();

      const message = input.value.trim();
      if (!message) {
        setText(output, "Escribe una consulta.");
        return;
      }

      if (button) button.disabled = true;
      setText(output, "Consultando SIP-AI…");

      try {
        const result = await api.chat(message);
        const answer = result?.answer || "El backend respondió sin contenido.";
        setText(output, answer);
      } catch (error) {
        setText(
          output,
          `Backend no disponible: ${error.message}. La interfaz permanece operativa.`
        );
      } finally {
        if (button) button.disabled = false;
      }
    }

    input.addEventListener("input", updateCount);

    if (form) {
      form.addEventListener("submit", submit);
    } else if (button) {
      button.addEventListener("click", submit);
    }

    updateCount();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
