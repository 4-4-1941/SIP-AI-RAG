(() => {
  "use strict";

  const META_URL =
    "data/metadata/adulto-mayor/nts-207-minsa-dgiesp-2023.json";

  const API = window.SIP_API || null;

  const CONFIG = window.SIP_CONFIG || {
    MAX_QUERY_LENGTH: 1200
  };

  let metadata = null;

  const $ = (id) => document.getElementById(id);

  const escapeHtml = (value) =>
    String(value ?? "").replace(/[&<>"']/g, (char) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    })[char]);

  function getOfficialUrl(data) {
    const sources = Array.isArray(data?.fuentes_oficiales)
      ? data.fuentes_oficiales
      : [];

    const source = sources.find(
      (item) => item && item.url
    );

    return source?.url || "";
  }

  function setLibraryStatus(text, className = "") {
    const status = $("libraryStatus");

    if (!status) {
      return;
    }

    status.textContent = text;
    status.className =
      `status ${className}`.trim();
  }

  function renderMetadata(data) {
    const container = $("metadata");

    if (!container) {
      return;
    }

    const modifications =
      data?.vigencia?.modificatorias ||
      data?.modificatorias ||
      [];

    const annexes =
      data?.anexos_prioritarios ||
      data?.anexos ||
      [];

    const officialUrl =
      getOfficialUrl(data);

    container.innerHTML = `
      <div class="grid">

        <div class="card">
          <b>
            ${escapeHtml(
              data.numero_norma || "Norma"
            )}
          </b>

          <span>
            ${escapeHtml(
              data.titulo || ""
            )}
          </span>
        </div>

        <div class="card">
          <b>Resolución</b>

          <span>
            ${escapeHtml(
              data.resolucion_aprobatoria ||
              data.resolucion ||
              "No registrada"
            )}
          </span>
        </div>

        <div class="card">
          <b>Validación</b>

          <span>
            ${escapeHtml(
              data.estado_validacion ||
              "No registrada"
            )}
          </span>
        </div>

      </div>

      <div class="source">

        <b>Modificatorias:</b>

        ${
          modifications.length
            ? modifications
                .map((item) =>
                  escapeHtml(
                    item.resolucion ||
                    item.numero_norma ||
                    ""
                  )
                )
                .join(" · ")
            : "No registradas"
        }

        <br>

        <b>Anexos priorizados:</b>

        ${
          annexes.length
            ? annexes
                .map((item) =>
                  escapeHtml(
                    item.anexo ||
                    item.nombre ||
                    ""
                  )
                )
                .join(" · ")
            : "No registrados"
        }

        <br>

        ${
          officialUrl
            ? `
              <a
                href="${escapeHtml(officialUrl)}"
                target="_blank"
                rel="noopener"
              >
                Abrir fuente oficial MINSA
              </a>
            `
            : ""
        }

      </div>
    `;
  }

  function localSearch(query) {
    if (!metadata) {
      return {
        found: false,
        html:
          "La biblioteca todavía no está cargada."
      };
    }

    const normalized =
      query.trim().toLowerCase();

    if (!normalized) {
      return {
        found: false,
        html:
          "Escribe un término de búsqueda."
      };
    }

    const terms =
      normalized
        .split(/\s+/)
        .filter(Boolean);

    const metadataText =
      JSON.stringify(metadata)
        .toLowerCase();

    const found =
      terms.every((term) =>
        metadataText.includes(term)
      );

    if (!found) {
      return {
        found: false,

        html: `
          Sin coincidencia documental para
          <b>
            ${escapeHtml(normalized)}
          </b>.

          No se genera contenido fuera
          de la fuente cargada.
        `
      };
    }

    const subtopics =
      (metadata.subtemas || [])
        .filter((item) =>
          terms.some((term) =>
            String(item)
              .toLowerCase()
              .includes(term)
          )
        );

    const annexes =
      (
        metadata.anexos_prioritarios ||
        metadata.anexos ||
        []
      ).filter((item) =>
        terms.some((term) =>
          JSON.stringify(item)
            .toLowerCase()
            .includes(term)
        )
      );

    const officialUrl =
      getOfficialUrl(metadata);

    return {
      found: true,

      html: `
        <b>Evidencia encontrada</b>

        <br>

        ${escapeHtml(
          metadata.numero_norma || ""
        )}

        <br>

        ${escapeHtml(
          metadata.titulo || ""
        )}

        ${
          subtopics.length
            ? `
              <br><br>

              <b>Subtemas:</b>

              <br>

              ${subtopics
                .map(escapeHtml)
                .join("<br>")}
            `
            : ""
        }

        ${
          annexes.length
            ? `
              <br><br>

              <b>Anexos relacionados:</b>

              <br>

              ${annexes
                .map((item) =>
                  escapeHtml(
                    `${item.anexo || ""} — ${
                      item.nombre ||
                      item.tema ||
                      ""
                    }`
                  )
                )
                .join("<br>")}
            `
            : ""
        }

        <div class="source">

          Estado:
          ${escapeHtml(
            metadata.estado_validacion || ""
          )}

          ${
            officialUrl
              ? `
                ·

                <a
                  href="${escapeHtml(
                    officialUrl
                  )}"
                  target="_blank"
                  rel="noopener"
                >
                  Fuente oficial
                </a>
              `
              : ""
          }

        </div>
      `
    };
  }

  async function loadMetadata() {
    try {
      const response =
        await fetch(
          META_URL,
          {
            cache: "no-store"
          }
        );

      if (!response.ok) {
        throw new Error(
          `HTTP ${response.status}`
        );
      }

      metadata =
        await response.json();

      setLibraryStatus(
        "Operativa · 1 fuente cargada",
        "ok"
      );

      renderMetadata(metadata);

    } catch (error) {

      setLibraryStatus(
        "Error de carga",
        "warn"
      );

      const container =
        $("metadata");

      if (container) {
        container.textContent =
          `No se pudo cargar ${META_URL}: ${error.message}`;
      }
    }
  }

  function handleLibrarySearch() {
    const input =
      $("search");

    const result =
      $("result");

    if (!input || !result) {
      return;
    }

    result.innerHTML =
      localSearch(input.value).html;
  }

  async function handleAssistantSubmit(event) {
    if (event) {
      event.preventDefault();
    }

    const input =
      $("q") ||
      $("queryInput");

    const output =
      $("out");

    const button =
      $("send") ||
      document.querySelector(
        '#queryForm button[type="submit"]'
      );

    if (!input || !output) {
      return;
    }

    const message =
      input.value.trim();

    if (!message) {
      output.textContent =
        "Escribe una consulta.";

      return;
    }

    if (button) {
      button.disabled = true;
    }

    const local =
      localSearch(message);

    if (
      local.found ||
      !API?.chat
    ) {
      output.innerHTML =
        local.html;

      if (button) {
        button.disabled = false;
      }

      return;
    }

    output.textContent =
      "Consultando SIP-AI…";

    try {

      const response =
        await API.chat(message);

      output.textContent =
        response?.answer ||
        "El backend respondió sin contenido.";

    } catch (error) {

      output.innerHTML = `
        ${local.html}

        <div class="source">
          Backend no disponible:
          ${escapeHtml(
            error.message
          )}
        </div>
      `;

    } finally {

      if (button) {
        button.disabled = false;
      }
    }
  }

  function init() {
    const searchInput =
      $("search");

    const searchButton =
      $("searchBtn");

    if (searchButton) {
      searchButton.addEventListener(
        "click",
        handleLibrarySearch
      );
    }

    if (searchInput) {
      searchInput.addEventListener(
        "keydown",
        (event) => {
          if (event.key === "Enter") {
            handleLibrarySearch();
          }
        }
      );
    }

    const assistantInput =
      $("q") ||
      $("queryInput");

    const assistantForm =
      $("queryForm");

    const assistantButton =
      $("send") ||
      document.querySelector(
        '#queryForm button[type="submit"]'
      );

    if (assistantInput) {
      assistantInput.maxLength =
        CONFIG.MAX_QUERY_LENGTH ||
        1200;
    }

    if (assistantForm) {

      assistantForm.addEventListener(
        "submit",
        handleAssistantSubmit
      );

    } else if (assistantButton) {

      assistantButton.addEventListener(
        "click",
        handleAssistantSubmit
      );
    }

    loadMetadata();
  }

  if (
    document.readyState === "loading"
  ) {

    document.addEventListener(
      "DOMContentLoaded",
      init
    );

  } else {

    init();
  }

})();
