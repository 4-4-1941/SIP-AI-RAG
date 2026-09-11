(() => {
  "use strict";

  const META_URL = "data/metadata/adulto-mayor/nts-207-minsa-dgiesp-2023.json";
  const API = window.SIP_API || null;
  const CONFIG = window.SIP_CONFIG || { MAX_QUERY_LENGTH: 1200 };

  let metadata = null;

  const $ = (id) => document.getElementById(id);

  const esc = (v) =>
    String(v ?? "").replace(/[&<>"']/g, (c) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    })[c]);

  const arr = (v) => Array.isArray(v) ? v : [];

  const norm = (v) =>
    String(v ?? "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase();

  function officialSources() {
    return arr(metadata?.fuentes_oficiales);
  }

  function officialUrl() {
    return officialSources().find((s) => s?.url)?.url || "";
  }

  function statusClass(v) {
    return norm(v).includes("validado_oficial")
      ? "ok"
      : "pending";
  }

  function switchView(name) {
    document.querySelectorAll(".view").forEach((view) => {
      view.classList.toggle(
        "active",
        view.id === `view-${name}`
      );
    });

    document.querySelectorAll(".nav-btn").forEach((button) => {
      button.classList.toggle(
        "active",
        button.dataset.view === name
      );
    });
  }

  function renderHeader() {
    $("sourceCount").textContent = metadata ? "1" : "0";

    $("annexCount").textContent =
      arr(metadata?.anexos_prioritarios).length;

    $("validationState").textContent =
      metadata?.estado_validacion || "—";

    const status = $("libraryStatus");

    status.textContent = metadata
      ? "Biblioteca operativa · 1 fuente"
      : "Biblioteca no disponible";

    status.className = metadata
      ? "status-badge"
      : "status-badge warn";
  }

  function renderQuickTerms() {
    const terms = [
      "VACAM",
      "adulto mayor",
      "RM 789",
      "RM 948",
      "fragilidad",
      "plan de cuidado"
    ];

    $("quickTerms").innerHTML = terms
      .map(
        (term) => `
          <button
            class="chip"
            type="button"
            data-query="${esc(term)}"
          >
            ${esc(term)}
          </button>
        `
      )
      .join("");

    $("quickTerms")
      .querySelectorAll(".chip")
      .forEach((button) => {
        button.addEventListener("click", () => {
          $("search").value = button.dataset.query;
          runSearch(button.dataset.query);
        });
      });
  }

  function renderMetadata() {
    const modifications =
      arr(metadata?.vigencia?.modificatorias);

    const annexes =
      arr(metadata?.anexos_prioritarios);

    const sources =
      officialSources();

    $("metadata").innerHTML = `
      <div class="metadata-grid">

        <article class="meta-card">
          <span class="eyebrow">Documento</span>

          <h3>
            ${esc(metadata?.numero_norma)}
          </h3>

          <p>
            ${esc(metadata?.titulo)}
          </p>
        </article>

        <article class="meta-card">
          <span class="eyebrow">Aprobación</span>

          <h3>
            ${esc(
              metadata?.resolucion_aprobatoria ||
              "No registrada"
            )}
          </h3>

          <p>
            Institución:
            ${esc(metadata?.institucion)}
          </p>
        </article>

        <article class="meta-card">
          <span class="eyebrow">
            Vigencia registrada
          </span>

          <h3>
            ${esc(
              metadata?.vigencia?.estado ||
              "No registrada"
            )}
          </h3>

          <p>
            ${
              modifications.length
                ? modifications
                    .map(
                      (m) =>
                        `${esc(m.resolucion)} · ${esc(m.alcance)}`
                    )
                    .join("<br>")
                : "Sin modificatorias registradas."
            }
          </p>
        </article>

        <article class="meta-card">
          <span class="eyebrow">Alcance</span>

          <h3>
            ${esc(
              metadata?.alcance_profesional ||
              "No registrado"
            )}
          </h3>

          <p>
            Bloque SERUMS:
            ${esc(
              metadata?.bloque_SERUMS ||
              "No registrado"
            )}
          </p>
        </article>

      </div>

      <div class="trace">
        <b>Trazabilidad:</b>
        documento oficial →
        metadatos →
        anexo/sección →
        conocimiento →
        recurso pedagógico →
        entrenamiento/herramienta →
        fuente original.
      </div>

      <div class="metadata-grid">

        ${annexes
          .map(
            (a) => `
              <article class="meta-card">

                <span class="tag ${statusClass(
                  a.estado_validacion
                )}">
                  ${esc(a.estado_validacion)}
                </span>

                <h3>
                  ${esc(a.anexo)} ·
                  ${esc(a.nombre)}
                </h3>

                <p>
                  ${esc(a.nota || "")}
                </p>

              </article>
            `
          )
          .join("")}

        ${sources
          .map(
            (s) => `
              <article class="meta-card">

                <span class="tag ok">
                  ${esc(s.estado_validacion)}
                </span>

                <h3>
                  ${esc(s.documento)}
                </h3>

                <p>
                  ${esc(s.rol_evidencia)}
                </p>

                <a
                  class="source-link"
                  href="${esc(s.url)}"
                  target="_blank"
                  rel="noopener"
                >
                  Abrir fuente oficial ↗
                </a>

              </article>
            `
          )
          .join("")}

      </div>
    `;
  }

  function renderLearning() {
    const resources =
      metadata?.recursos_pedagogicos || {};

    const cards =
      Object.values(resources);

    $("learningResources").innerHTML =
      cards.length
        ? `
          <div class="resource-grid">

            ${cards
              .map(
                (resource) => `
                  <article class="resource-card">

                    <span class="tag ${statusClass(
                      resource.estado
                    )}">
                      ${esc(resource.estado)}
                    </span>

                    <h3>
                      ${esc(resource.titulo)}
                    </h3>

                    <p>
                      <b>ID:</b>
                      ${esc(resource.id)}
                    </p>

                    <p>
                      ${esc(resource.motivo || "")}
                    </p>

                    <p class="muted">
                      El recurso permanece bloqueado
                      para publicación mientras la
                      evidencia detallada no esté
                      aprobada.
                    </p>

                  </article>
                `
              )
              .join("")}

          </div>
        `
        : `
          <div class="empty-state">
            <strong>
              Sin recursos cargados
            </strong>

            <p>
              No hay recursos pedagógicos
              registrados en esta fuente.
            </p>
          </div>
        `;
  }

  function searchableRecords() {
    if (!metadata) {
      return [];
    }

    return [
      {
        type: "Norma",
        title: metadata.numero_norma,
        text: [
          metadata.titulo,
          metadata.tema,
          ...arr(metadata.subtemas)
        ].join(" "),
        state: metadata.estado_validacion,
        detail: metadata.titulo,
        url: officialUrl()
      },

      ...arr(
        metadata?.vigencia?.modificatorias
      ).map((item) => ({
        type: "Modificatoria",
        title: item.resolucion,
        text:
          `${item.resolucion} ${item.alcance}`,
        state: "VALIDADO_OFICIAL",
        detail: item.alcance,
        url:
          officialSources().find(
            (source) =>
              source.documento ===
              item.resolucion
          )?.url ||
          officialUrl()
      })),

      ...arr(
        metadata?.anexos_prioritarios
      ).map((item) => ({
        type: "Anexo",
        title:
          `${item.anexo} · ${item.nombre}`,
        text:
          `${item.anexo} ${item.nombre} ${item.nota || ""}`,
        state: item.estado_validacion,
        detail: item.nota || "",
        url: officialUrl()
      })),

      ...arr(
        metadata?.subtemas
      ).map((subtopic) => ({
        type: "Subtema",
        title: subtopic,
        text: subtopic,
        state: metadata.estado_validacion,
        detail:
          `Subtema registrado en ${metadata.numero_norma}.`,
        url: officialUrl()
      }))
    ];
  }

  function searchRecords(query) {
    const terms =
      norm(query)
        .split(/\s+/)
        .filter(Boolean);

    if (!terms.length) {
      return [];
    }

    return searchableRecords()
      .map((record) => {
        const haystack =
          norm(
            `${record.title} ${record.text} ${record.detail}`
          );

        const hits =
          terms.filter(
            (term) =>
              haystack.includes(term)
          ).length;

        return {
          ...record,
          score: hits
        };
      })
      .filter(
        (record) =>
          record.score > 0
      )
      .sort(
        (a, b) =>
          b.score - a.score
      );
  }

  function resultHtml(records, query) {
    if (!records.length) {
      return `
        <div class="empty-state">

          <strong>
            EVIDENCIA_INSUFICIENTE
          </strong>

          <p>
            No hay coincidencia documental
            para “${esc(query)}”
            en la fuente cargada.
            No se completa con contenido externo.
          </p>

        </div>
      `;
    }

    return records
      .map(
        (record) => `
          <article class="evidence-card">

            <div class="tag-row">

              <span class="tag">
                ${esc(record.type)}
              </span>

              <span class="tag ${statusClass(
                record.state
              )}">
                ${esc(record.state)}
              </span>

            </div>

            <h3>
              ${esc(record.title)}
            </h3>

            <p>
              ${esc(record.detail)}
            </p>

            ${
              record.url
                ? `
                  <a
                    class="source-link"
                    href="${esc(record.url)}"
                    target="_blank"
                    rel="noopener"
                  >
                    Ver fuente oficial ↗
                  </a>
                `
                : ""
            }

          </article>
        `
      )
      .join("");
  }

  function runSearch(query) {
    const value =
      String(query || "").trim();

    $("result").className =
      "results";

    $("result").innerHTML =
      value
        ? resultHtml(
            searchRecords(value),
            value
          )
        : `
          <div class="empty-state">

            <strong>
              Escribe una consulta
            </strong>

            <p>
              La búsqueda no puede estar vacía.
            </p>

          </div>
        `;
  }

  function addMessage(
    role,
    title,
    text
  ) {
    const container =
      document.createElement("div");

    container.className =
      `message ${role}`;

    container.innerHTML = `
      <span class="avatar">
        ${
          role === "user"
            ? "TÚ"
            : "SIP"
        }
      </span>

      <div>

        <strong>
          ${esc(title)}
        </strong>

        <p>
          ${esc(text)}
        </p>

      </div>
    `;

    $("out").appendChild(container);

    container.scrollIntoView({
      behavior: "smooth",
      block: "nearest"
    });
  }

  async function assistantQuery(message) {
    addMessage(
      "user",
      "Consulta",
      message
    );

    const local =
      searchRecords(message);

    if (local.length) {
      const summary =
        local
          .slice(0, 4)
          .map(
            (record) =>
              `${record.type}: ${record.title} — ${record.detail}`
          )
          .join("\n\n");

      addMessage(
        "system",
        "Evidencia documental",
        summary
      );

      return;
    }

    if (
      !API?.chat ||
      !window.SIP_CONFIG?.API_BASE_URL
    ) {
      addMessage(
        "system",
        "EVIDENCIA_INSUFICIENTE",
        "La biblioteca local no contiene evidencia suficiente y el backend RAG aún no está desplegado. No se genera una respuesta no sustentada."
      );

      return;
    }

    try {
      const response =
        await API.chat(message);

      addMessage(
        "system",
        "Respuesta RAG",
        response?.answer ||
        "El backend respondió sin contenido."
      );
    } catch (error) {
      addMessage(
        "system",
        "Backend no disponible",
        error.message
      );
    }
  }

  async function checkBackend() {
    const badge =
      $("backendStatus");

    if (
      !API?.health ||
      !window.SIP_CONFIG?.API_BASE_URL
    ) {
      badge.textContent =
        "Backend pendiente";

      badge.className =
        "mini-status warn";

      return;
    }

    try {
      const health =
        await API.health();

      badge.textContent =
        health?.rag_active
          ? "RAG activo"
          : "API activa · RAG sin índice";

      badge.className =
        "mini-status";

    } catch (_) {
      badge.textContent =
        "Backend no disponible";

      badge.className =
        "mini-status warn";
    }
  }

  async function load() {
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

      renderHeader();
      renderQuickTerms();
      renderMetadata();
      renderLearning();

    } catch (error) {
      renderHeader();

      $("result").innerHTML = `
        <div class="empty-state">

          <strong>
            No se pudo cargar la biblioteca
          </strong>

          <p>
            ${esc(error.message)}
          </p>

        </div>
      `;
    }

    checkBackend();
  }

  function init() {
    document
      .querySelectorAll(".nav-btn")
      .forEach((button) => {
        button.addEventListener(
          "click",
          () =>
            switchView(
              button.dataset.view
            )
        );
      });

    $("searchForm").addEventListener(
      "submit",
      (event) => {
        event.preventDefault();

        runSearch(
          $("search").value
        );
      }
    );

    $("queryForm").addEventListener(
      "submit",
      async (event) => {
        event.preventDefault();

        const input =
          $("q");

        const message =
          input.value.trim();

        if (!message) {
          return;
        }

        input.value = "";

        await assistantQuery(
          message
        );
      }
    );

    $("q").maxLength =
      CONFIG.MAX_QUERY_LENGTH ||
      1200;

    load();
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
