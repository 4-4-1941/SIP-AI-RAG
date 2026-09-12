(() => {
"use strict";

const CATALOG_URL = "data/metadata/catalog.json";
const SERUMS_MANIFEST_URL =
  "knowledge/minsa/serums-2026-ii/manifest.json";

const API = window.SIP_API || null;
const CONFIG =
  window.SIP_CONFIG || { MAX_QUERY_LENGTH: 1200 };

let catalog = null;
let documents = [];
let activeDocument = null;
let serumsManifest = null;

const $ = (id) => document.getElementById(id);
const arr = (v) => Array.isArray(v) ? v : [];

const esc = (v) =>
  String(v ?? "").replace(
    /[&<>"']/g,
    (c) =>
      ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
      })[c]
  );

const norm = (v) =>
  String(v ?? "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase();

function statusClass(value) {
  const v = norm(value);

  if (v.includes("validado_oficial")) {
    return "ok";
  }

  if (v.includes("no_aprobado")) {
    return "warn";
  }

  return "pending";
}

function officialSources(doc) {
  return arr(doc?.fuentes_oficiales);
}

function officialUrl(doc) {
  return (
    doc?.url_oficial ||
    officialSources(doc).find((s) => s?.url)?.url ||
    ""
  );
}

function documentLabel(doc) {
  return (
    doc?.numero_norma ||
    doc?.resolucion_aprobatoria ||
    doc?.titulo ||
    doc?.id ||
    "Documento"
  );
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
  const corpusTotal =
    serumsManifest?.documentos_unicos || documents.length;

  const compendiaTotal =
    serumsManifest?.compendios_descubiertos || 0;

  if ($("sourceCount")) {
    $("sourceCount").textContent = corpusTotal;
  }

  if ($("annexCount")) {
    $("annexCount").textContent =
      documents.reduce(
        (total, doc) =>
          total + arr(doc?.anexos_prioritarios).length,
        0
      );
  }

  if ($("validationState")) {
    $("validationState").textContent =
      corpusTotal
        ? "BIBLIOTECA SERUMS"
        : "—";
  }

  const status = $("libraryStatus");

  if (status) {
    status.textContent =
      corpusTotal
        ? `Bibliografía SERUMS · ${corpusTotal} documentos · ${compendiaTotal} compendios`
        : "Biblioteca no disponible";

    status.className =
      corpusTotal
        ? "status-badge"
        : "status-badge warn";
  }
}

function renderQuickTerms() {
  const container = $("quickTerms");

  if (!container) return;

  const terms = [
    ...new Set(
      documents
        .flatMap((doc) => [
          doc.tema,
          doc.bloque_SERUMS,
          ...arr(doc.subtemas),
          ...arr(doc.compendios_origen)
        ])
        .filter(Boolean)
    )
  ]
    .filter(
      (term) =>
        !/^ver las? \d+ normas?$/i.test(String(term))
    )
    .slice(0, 16);

  container.innerHTML = terms
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

  container
    .querySelectorAll(".chip")
    .forEach((button) => {
      button.addEventListener("click", () => {
        const query = button.dataset.query || "";

        if ($("search")) {
          $("search").value = query;
        }

        runSearch(query);
      });
    });
}

function renderMetadata() {
  const target = $("metadata");

  if (!target) return;

  if (!activeDocument) {
    target.innerHTML = `
      <div class="empty-state">
        <strong>Sin documento activo</strong>
      </div>
    `;
    return;
  }

  const modifications =
    arr(activeDocument?.vigencia?.modificatorias);

  const annexes =
    arr(activeDocument?.anexos_prioritarios);

  const sources =
    officialSources(activeDocument);

  const isCorpus =
    Boolean(activeDocument._serumsCorpus);

  target.innerHTML = `
    <div
      style="
        display:flex;
        gap:12px;
        align-items:center;
        justify-content:space-between;
        flex-wrap:wrap;
        margin-bottom:16px
      "
    >
      <div>
        <span class="eyebrow">
          Documento activo
        </span>

        <h3 style="margin:.25rem 0 0">
          ${esc(documentLabel(activeDocument))}
        </h3>
      </div>

      <select
        id="documentSelector"
        aria-label="Seleccionar documento"
      >
        ${documents
          .map(
            (doc) => `
              <option
                value="${esc(doc.id)}"
                ${
                  doc.id === activeDocument.id
                    ? "selected"
                    : ""
                }
              >
                ${esc(documentLabel(doc))}
              </option>
            `
          )
          .join("")}
      </select>
    </div>

    <div class="metadata-grid">

      <article class="meta-card">
        <span class="eyebrow">
          Documento
        </span>

        <h3>
          ${esc(
            activeDocument.titulo ||
            documentLabel(activeDocument)
          )}
        </h3>

        <p>
          ${esc(
            activeDocument.tema ||
            "Bibliografía oficial SERUMS 2026-II"
          )}
        </p>
      </article>

      <article class="meta-card">
        <span class="eyebrow">
          Estado documental
        </span>

        <h3>
          ${esc(
            activeDocument.estado_validacion ||
            "No registrado"
          )}
        </h3>

        <p>
          ${
            isCorpus
              ? activeDocument.archivo_rag
                ? "Texto materializado para RAG."
                : "Documento oficial identificado; texto pendiente de extracción."
              : modifications.length
                ? modifications
                    .map(
                      (item) =>
                        `${esc(item.resolucion)} · ${esc(
                          item.alcance || ""
                        )}`
                    )
                    .join("<br>")
                : "Sin modificatorias cargadas."
          }
        </p>
      </article>

      <article class="meta-card">
        <span class="eyebrow">
          Origen
        </span>

        <h3>
          ${esc(
            isCorpus
              ? "SERUMS 2026-II"
              : activeDocument.bloque_SERUMS ||
                "Biblioteca SIP"
          )}
        </h3>

        <p>
          ${esc(
            arr(activeDocument.compendios_origen)
              .join(" · ") ||
            activeDocument.alcance_profesional ||
            ""
          )}
        </p>
      </article>

    </div>

    <div class="trace">
      <b>Trazabilidad:</b>
      documento oficial →
      metadatos →
      página/sección/anexo →
      conocimiento extraído →
      recurso pedagógico →
      entrenamiento/herramienta →
      fuente original.
    </div>

    <div class="metadata-grid">

      ${annexes
        .map(
          (item) => `
            <article class="meta-card">

              <span
                class="tag ${statusClass(
                  item.estado_validacion
                )}"
              >
                ${esc(item.estado_validacion)}
              </span>

              <h3>
                ${esc(item.anexo)}
                ·
                ${esc(item.nombre)}
              </h3>

              <p>
                ${esc(item.nota || "")}
              </p>

            </article>
          `
        )
        .join("")}

      ${sources
        .map(
          (source) => `
            <article class="meta-card">

              <span
                class="tag ${statusClass(
                  source.estado_validacion
                )}"
              >
                ${esc(source.estado_validacion)}
              </span>

              <h3>
                ${esc(source.documento)}
              </h3>

              <p>
                ${esc(
                  source.rol_evidencia ||
                  "Fuente oficial"
                )}
              </p>

              ${
                source.url
                  ? `
                    <a
                      class="source-link"
                      href="${esc(source.url)}"
                      target="_blank"
                      rel="noopener"
                    >
                      Abrir fuente oficial ↗
                    </a>
                  `
                  : ""
              }

            </article>
          `
        )
        .join("")}

      ${
        isCorpus && activeDocument.url_oficial
          ? `
            <article class="meta-card">

              <span
                class="tag ${statusClass(
                  activeDocument.estado_validacion
                )}"
              >
                ${esc(
                  activeDocument.estado_validacion
                )}
              </span>

              <h3>
                Fuente oficial MINSA
              </h3>

              <p>
                ${
                  activeDocument.archivo_rag
                    ? "Documento incorporado al corpus RAG."
                    : "Extracción de texto pendiente."
                }
              </p>

              <a
                class="source-link"
                href="${esc(
                  activeDocument.url_oficial
                )}"
                target="_blank"
                rel="noopener"
              >
                Abrir fuente oficial ↗
              </a>

              ${
                activeDocument.pdf_oficial
                  ? `
                    <a
                      class="source-link"
                      href="${esc(
                        activeDocument.pdf_oficial
                      )}"
                      target="_blank"
                      rel="noopener"
                    >
                      PDF oficial ↗
                    </a>
                  `
                  : ""
              }

            </article>
          `
          : ""
      }

    </div>
  `;

  $("documentSelector")
    ?.addEventListener(
      "change",
      (event) => {
        selectDocument(event.target.value);
      }
    );
                              }
  function renderLearning() {
  const target = $("learningResources");

  if (!target) return;

  const resources =
    documents.flatMap((doc) =>
      Object.values(
        doc.recursos_pedagogicos || {}
      ).map((resource) => ({
        ...resource,
        document: documentLabel(doc)
      }))
    );

  target.innerHTML =
    resources.length
      ? `
        <div class="resource-grid">
          ${resources
            .map(
              (resource) => `
                <article class="resource-card">

                  <span
                    class="tag ${statusClass(
                      resource.estado
                    )}"
                  >
                    ${esc(resource.estado)}
                  </span>

                  <h3>
                    ${esc(resource.titulo)}
                  </h3>

                  <p>
                    <b>
                      ${esc(resource.document)}
                    </b>
                    ·
                    ${esc(resource.id)}
                  </p>

                  <p>
                    ${esc(resource.motivo || "")}
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
            Sin recursos pedagógicos cargados
          </strong>
        </div>
      `;
}

function searchableRecords() {
  return documents.flatMap((doc) => [
    {
      type:
        doc._serumsCorpus
          ? "SERUMS 2026-II"
          : "Documento",

      title:
        documentLabel(doc),

      text: [
        doc.titulo,
        doc.tema,
        doc.bloque_SERUMS,
        ...arr(doc.subtemas),
        ...arr(doc.compendios_origen)
      ].join(" "),

      state:
        doc.estado_validacion,

      detail:
        doc._serumsCorpus
          ? doc.archivo_rag
            ? "Documento oficial materializado para RAG."
            : "Documento oficial identificado; extracción de texto pendiente."
          : doc.titulo,

      url:
        officialUrl(doc),

      docId:
        doc.id
    },

    ...arr(
      doc?.vigencia?.modificatorias
    ).map((item) => ({
      type: "Modificatoria",

      title:
        item.resolucion,

      text:
        `${item.resolucion} ${item.alcance || ""}`,

      state:
        "VALIDADO_OFICIAL",

      detail:
        item.alcance || "",

      url:
        officialSources(doc)
          .find(
            (source) =>
              source.documento ===
              item.resolucion
          )
          ?.url ||
        officialUrl(doc),

      docId:
        doc.id
    })),

    ...arr(
      doc?.anexos_prioritarios
    ).map((item) => ({
      type: "Anexo",

      title:
        `${item.anexo} · ${item.nombre}`,

      text:
        `${item.anexo} ${item.nombre} ${item.nota || ""}`,

      state:
        item.estado_validacion,

      detail:
        item.nota || "",

      url:
        officialUrl(doc),

      docId:
        doc.id
    })),

    ...arr(doc.subtemas).map(
      (subtopic) => ({
        type: "Subtema",

        title:
          subtopic,

        text:
          `${subtopic} ${doc.titulo || ""} ${doc.tema || ""}`,

        state:
          doc.estado_validacion,

        detail:
          `Registrado en ${documentLabel(doc)}.`,

        url:
          officialUrl(doc),

        docId:
          doc.id
      })
    )
  ]);
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

      const score =
        terms.filter(
          (term) =>
            haystack.includes(term)
        ).length;

      return {
        ...record,
        score
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
          en la biblioteca cargada.
          No se completa con contenido externo.
        </p>

      </div>
    `;
  }

  return records
    .slice(0, 100)
    .map(
      (record) => `
        <article class="evidence-card">

          <div class="tag-row">

            <span class="tag">
              ${esc(record.type)}
            </span>

            <span
              class="tag ${statusClass(
                record.state
              )}"
            >
              ${esc(record.state)}
            </span>

          </div>

          <h3>
            ${esc(record.title)}
          </h3>

          <p>
            ${esc(record.detail)}
          </p>

          <button
            type="button"
            class="open-result-doc"
            data-id="${esc(record.docId)}"
          >
            Abrir documento
          </button>

          ${
            record.url
              ? `
                <a
                  class="source-link"
                  href="${esc(record.url)}"
                  target="_blank"
                  rel="noopener"
                >
                  Fuente oficial ↗
                </a>
              `
              : ""
          }

        </article>
      `
    )
    .join("");
}

function bindResultButtons() {
  document
    .querySelectorAll(".open-result-doc")
    .forEach((button) => {
      button.addEventListener(
        "click",
        () => {
          selectDocument(
            button.dataset.id
          );

          switchView("source");
        }
      );
    });
}

function runSearch(query) {
  const value =
    String(query || "").trim();

  const target =
    $("result");

  if (!target) return;

  target.className =
    "results";

  target.innerHTML =
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
        </div>
      `;

  bindResultButtons();
}

function selectDocument(id) {
  activeDocument =
    documents.find(
      (doc) =>
        String(doc.id) === String(id)
    ) ||
    documents[0] ||
    null;

  renderMetadata();
}

function addMessage(
  role,
  title,
  text
) {
  const output =
    $("out");

  if (!output) return;

  const container =
    document.createElement("div");

  container.className =
    `message ${role}`;

  container.innerHTML = `
    <span class="avatar">
      ${role === "user" ? "TÚ" : "SIP"}
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

  output.appendChild(container);

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
    addMessage(
      "system",
      "Evidencia documental",
      local
        .slice(0, 5)
        .map(
          (record) =>
            `${record.type}: ${record.title} — ${record.detail}`
        )
        .join("\n\n")
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

  if (!badge) return;

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
  async function loadLibrary() {
  try {
    const [
      catalogResponse,
      manifestResponse
    ] = await Promise.all([
      fetch(
        CATALOG_URL,
        { cache: "no-store" }
      ),

      fetch(
        SERUMS_MANIFEST_URL,
        { cache: "no-store" }
      )
    ]);

    if (!catalogResponse.ok) {
      throw new Error(
        `No se pudo cargar catalog.json · HTTP ${catalogResponse.status}`
      );
    }

    catalog =
      await catalogResponse.json();

    if (manifestResponse.ok) {
      serumsManifest =
        await manifestResponse.json();
    }

    const baseDocuments =
      await Promise.all(
        arr(catalog.documentos).map(
          async (item) => {
            try {
              const response =
                await fetch(
                  item.ruta,
                  { cache: "no-store" }
                );

              if (!response.ok) {
                throw new Error(
                  `HTTP ${response.status}`
                );
              }

              const doc =
                await response.json();

              if (!doc.id) {
                doc.id = item.id;
              }

              return doc;

            } catch (_) {
              return {
                ...item,

                estado_validacion:
                  item.estado ||
                  "NO_APROBADO",

                fuentes_oficiales: [],
                subtemas: [],
                anexos_prioritarios: []
              };
            }
          }
        )
      );

    const corpusDocuments =
      arr(
        serumsManifest?.documentos
      ).map(
        (doc, index) => {
          const safeId =
            doc.id ||
            `MINSA-SERUMS-2026-II-${index + 1}`;

          return {
            ...doc,

            id:
              safeId,

            _serumsCorpus:
              true,

            institucion:
              "Ministerio de Salud del Perú",

            tema:
              "Bibliografía oficial SERUMS 2026-II",

            bloque_SERUMS:
              "SERUMS 2026-II",

            fuentes_oficiales:
              doc.url_oficial
                ? [
                    {
                      documento:
                        doc.titulo ||
                        safeId,

                      url:
                        doc.url_oficial,

                      estado_validacion:
                        doc.estado_validacion,

                      rol_evidencia:
                        "Fuente oficial MINSA"
                    }
                  ]
                : [],

            subtemas:
              arr(doc.subtemas),

            anexos_prioritarios:
              arr(doc.anexos_prioritarios)
          };
        }
      );

    /*
     * Unificación sin duplicar documentos.
     *
     * Si un documento del catálogo base y otro del
     * corpus SERUMS apuntan a la misma URL oficial,
     * se conserva una sola entrada.
     */

    const documentMap =
      new Map();

    [
      ...baseDocuments.filter(Boolean),
      ...corpusDocuments
    ].forEach((doc) => {
      const key =
        doc.url_oficial ||
        officialUrl(doc) ||
        doc.id;

      if (!documentMap.has(key)) {
        documentMap.set(
          key,
          doc
        );
      }
    });

    documents =
      [...documentMap.values()];

    activeDocument =
      documents[0] || null;

    renderHeader();
    renderQuickTerms();
    renderMetadata();
    renderLearning();

  } catch (error) {
    const status =
      $("libraryStatus");

    if (status) {
      status.textContent =
        "Biblioteca no disponible";

      status.className =
        "status-badge warn";
    }

    const target =
      $("result");

    if (target) {
      target.innerHTML = `
        <div class="empty-state">

          <strong>
            Error de catálogo
          </strong>

          <p>
            ${esc(error.message)}
          </p>

        </div>
      `;
    }
  }

  checkBackend();
}

function bindNavigation() {
  document
    .querySelectorAll(".nav-btn")
    .forEach((button) => {
      button.addEventListener(
        "click",
        () => {
          switchView(
            button.dataset.view
          );
        }
      );
    });
}

function bindSearch() {
  const form =
    $("searchForm");

  if (!form) return;

  form.addEventListener(
    "submit",
    (event) => {
      event.preventDefault();

      runSearch(
        $("search")?.value || ""
      );
    }
  );
}

function bindAssistant() {
  const form =
    $("queryForm");

  if (!form) return;

  form.addEventListener(
    "submit",
    (event) => {
      event.preventDefault();

      const input =
        $("q");

      if (!input) return;

      const query =
        input.value
          .trim()
          .slice(
            0,
            CONFIG.MAX_QUERY_LENGTH ||
              1200
          );

      if (!query) return;

      input.value = "";

      assistantQuery(query);
    }
  );
}

function init() {
  bindNavigation();
  bindSearch();
  bindAssistant();

  loadLibrary();
}

if (
  document.readyState ===
  "loading"
) {
  document.addEventListener(
    "DOMContentLoaded",
    init
  );
} else {
  init();
}

})();
