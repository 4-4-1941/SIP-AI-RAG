(() => {
  "use strict";

  const CATALOG_URL = "data/metadata/catalog.json";
  const API = window.SIP_API || null;
  const CONFIG = window.SIP_CONFIG || { MAX_QUERY_LENGTH: 1200 };

  let catalog = null;
  let documents = [];
  let activeDocument = null;

  const $ = (id) => document.getElementById(id);
  const arr = (v) => Array.isArray(v) ? v : [];

  const esc = (v) =>
    String(v ?? "").replace(/[&<>"']/g, (c) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    })[c]);

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
    return officialSources(doc)
      .find((source) => source?.url)?.url || "";
  }

  function documentLabel(doc) {
    return (
      doc?.numero_norma ||
      doc?.resolucion_aprobatoria ||
      doc?.id ||
      "Documento"
    );
  }

  function switchView(name) {
    document
      .querySelectorAll(".view")
      .forEach((view) => {
        view.classList.toggle(
          "active",
          view.id === `view-${name}`
        );
      });

    document
      .querySelectorAll(".nav-btn")
      .forEach((button) => {
        button.classList.toggle(
          "active",
          button.dataset.view === name
        );
      });
  }

  function renderHeader() {
    $("sourceCount").textContent =
      documents.length;

    $("annexCount").textContent =
      documents.reduce(
        (total, doc) =>
          total +
          arr(doc?.anexos_prioritarios).length,
        0
      );

    $("validationState").textContent =
      documents.length
        ? "BIBLIOTECA MULTIDOCUMENTO"
        : "—";

    const status =
      $("libraryStatus");

    status.textContent =
      documents.length
        ? `Biblioteca operativa · ${documents.length} documentos`
        : "Biblioteca no disponible";

    status.className =
      documents.length
        ? "status-badge"
        : "status-badge warn";
  }

  function renderQuickTerms() {
    const terms = [
      ...new Set(
        documents
          .flatMap((doc) => [
            doc.tema,
            doc.bloque_SERUMS,
            ...arr(doc.subtemas)
          ])
          .filter(Boolean)
      )
    ].slice(0, 16);

    $("quickTerms").innerHTML =
      terms
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
        button.addEventListener(
          "click",
          () => {
            $("search").value =
              button.dataset.query;

            runSearch(
              button.dataset.query
            );
          }
        );
      });
  }

  function renderMetadata() {
    if (!activeDocument) {
      $("metadata").innerHTML = `
        <div class="empty-state">
          <strong>
            Sin documento activo
          </strong>
        </div>
      `;

      return;
    }

    const modifications =
      arr(
        activeDocument
          ?.vigencia
          ?.modificatorias
      );

    const annexes =
      arr(
        activeDocument
          ?.anexos_prioritarios
      );

    const sources =
      officialSources(
        activeDocument
      );

    $("metadata").innerHTML = `
      <div
        style="
          display:flex;
          gap:12px;
          align-items:center;
          justify-content:space-between;
          flex-wrap:wrap;
          margin-bottom:16px;
        "
      >
        <div>
          <span class="eyebrow">
            Documento activo
          </span>

          <h3
            style="
              margin:.25rem 0 0
            "
          >
            ${esc(
              documentLabel(
                activeDocument
              )
            )}
          </h3>
        </div>

        <select
          id="documentSelector"
          aria-label="Seleccionar documento"
        >
          ${
            documents
              .map(
                (doc) => `
                  <option
                    value="${esc(doc.id)}"
                    ${
                      doc.id ===
                      activeDocument.id
                        ? "selected"
                        : ""
                    }
                  >
                    ${esc(
                      documentLabel(doc)
                    )}
                  </option>
                `
              )
              .join("")
          }
        </select>
      </div>

      <div class="metadata-grid">

        <article class="meta-card">
          <span class="eyebrow">
            Documento
          </span>

          <h3>
            ${esc(
              activeDocument.titulo
            )}
          </h3>

          <p>
            ${esc(
              activeDocument.tema || ""
            )}
          </p>
        </article>

        <article class="meta-card">
          <span class="eyebrow">
            Aprobación
          </span>

          <h3>
            ${esc(
              activeDocument
                .resolucion_aprobatoria ||
              "No registrada"
            )}
          </h3>

          <p>
            ${esc(
              activeDocument
                .institucion ||
              ""
            )}
          </p>
        </article>

        <article class="meta-card">
          <span class="eyebrow">
            Estado documental
          </span>

          <h3>
            ${esc(
              activeDocument
                .estado_validacion ||
              "No registrado"
            )}
          </h3>

          <p>
            ${
              modifications.length
                ? modifications
                    .map(
                      (item) =>
                        `${esc(
                          item.resolucion
                        )} · ${esc(
                          item.alcance ||
                          ""
                        )}`
                    )
                    .join("<br>")
                : "Sin modificatorias cargadas."
            }
          </p>
        </article>

        <article class="meta-card">
          <span class="eyebrow">
            Bloque SERUMS
          </span>

          <h3>
            ${esc(
              activeDocument
                .bloque_SERUMS ||
              "No registrado"
            )}
          </h3>

          <p>
            ${esc(
              activeDocument
                .alcance_profesional ||
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
        conocimiento →
        recurso pedagógico →
        entrenamiento/herramienta →
        fuente original.
      </div>

      <div class="metadata-grid">

        ${
          annexes
            .map(
              (item) => `
                <article class="meta-card">

                  <span
                    class="tag ${
                      statusClass(
                        item.estado_validacion
                      )
                    }"
                  >
                    ${esc(
                      item.estado_validacion
                    )}
                  </span>

                  <h3>
                    ${esc(
                      item.anexo
                    )}
                    ·
                    ${esc(
                      item.nombre
                    )}
                  </h3>

                  <p>
                    ${esc(
                      item.nota || ""
                    )}
                  </p>

                </article>
              `
            )
            .join("")
        }

        ${
          sources
            .map(
              (source) => `
                <article class="meta-card">

                  <span
                    class="tag ${
                      statusClass(
                        source.estado_validacion
                      )
                    }"
                  >
                    ${esc(
                      source.estado_validacion
                    )}
                  </span>

                  <h3>
                    ${esc(
                      source.documento
                    )}
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
                          href="${esc(
                            source.url
                          )}"
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
            .join("")
        }

      </div>
    `;

    $("documentSelector")
      ?.addEventListener(
        "change",
        (event) => {
          selectDocument(
            event.target.value
          );
        }
      );
  }

  function renderLearning() {
    const resources =
      documents.flatMap(
        (doc) =>
          Object
            .values(
              doc.recursos_pedagogicos ||
              {}
            )
            .map(
              (resource) => ({
                ...resource,
                document:
                  documentLabel(doc)
              })
            )
      );

    $("learningResources").innerHTML =
      resources.length
        ? `
          <div class="resource-grid">

            ${
              resources
                .map(
                  (resource) => `
                    <article
                      class="resource-card"
                    >

                      <span
                        class="tag ${
                          statusClass(
                            resource.estado
                          )
                        }"
                      >
                        ${esc(
                          resource.estado
                        )}
                      </span>

                      <h3>
                        ${esc(
                          resource.titulo
                        )}
                      </h3>

                      <p>
                        <b>
                          ${esc(
                            resource.document
                          )}
                        </b>
                        ·
                        ${esc(
                          resource.id
                        )}
                      </p>

                      <p>
                        ${esc(
                          resource.motivo ||
                          ""
                        )}
                      </p>

                    </article>
                  `
                )
                .join("")
            }

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
    return documents.flatMap(
      (doc) => [

        {
          type: "Documento",

          title:
            documentLabel(doc),

          text: [
            doc.titulo,
            doc.tema,
            doc.bloque_SERUMS,
            ...arr(doc.subtemas)
          ].join(" "),

          state:
            doc.estado_validacion,

          detail:
            doc.titulo,

          url:
            officialUrl(doc),

          docId:
            doc.id
        },

        ...arr(
          doc
            ?.vigencia
            ?.modificatorias
        ).map(
          (item) => ({
            type:
              "Modificatoria",

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
          })
        ),

        ...arr(
          doc
            ?.anexos_prioritarios
        ).map(
          (item) => ({
            type:
              "Anexo",

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
          })
        ),

        ...arr(
          doc.subtemas
        ).map(
          (subtopic) => ({
            type:
              "Subtema",

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

      ]
    );
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
      .map(
        (record) => {
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
        }
      )
      .filter(
        (record) =>
          record.score > 0
      )
      .sort(
        (a, b) =>
          b.score - a.score
      );
  }

  function resultHtml(
    records,
    query
  ) {
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
      .map(
        (record) => `
          <article
            class="evidence-card"
          >

            <div class="tag-row">

              <span class="tag">
                ${esc(
                  record.type
                )}
              </span>

              <span
                class="tag ${
                  statusClass(
                    record.state
                  )
                }"
              >
                ${esc(
                  record.state
                )}
              </span>

            </div>

            <h3>
              ${esc(
                record.title
              )}
            </h3>

            <p>
              ${esc(
                record.detail
              )}
            </p>

            <button
              type="button"
              class="open-result-doc"
              data-id="${esc(
                record.docId
              )}"
            >
              Abrir documento
            </button>

            ${
              record.url
                ? `
                  <a
                    class="source-link"
                    href="${esc(
                      record.url
                    )}"
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
      .querySelectorAll(
        ".open-result-doc"
      )
      .forEach(
        (button) => {
          button.addEventListener(
            "click",
            () => {
              selectDocument(
                button.dataset.id
              );

              switchView(
                "source"
              );
            }
          );
        }
      );
  }

  function runSearch(query) {
    const value =
      String(query || "")
        .trim();

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
          </div>
        `;

    bindResultButtons();
  }

  function selectDocument(id) {
    activeDocument =
      documents.find(
        (doc) =>
          doc.id === id
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
    const container =
      document.createElement(
        "div"
      );

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

    $("out")
      .appendChild(
        container
      );

    container.scrollIntoView({
      behavior:
        "smooth",

      block:
        "nearest"
    });
  }

  async function assistantQuery(
    message
  ) {
    addMessage(
      "user",
      "Consulta",
      message
    );

    const local =
      searchRecords(
        message
      );

    if (local.length) {
      const summary =
        local
          .slice(0, 5)
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
      !window
        .SIP_CONFIG
        ?.API_BASE_URL
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
        await API.chat(
          message
        );

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
      !window
        .SIP_CONFIG
        ?.API_BASE_URL
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
      const catalogResponse =
        await fetch(
          CATALOG_URL,
          {
            cache:
              "no-store"
          }
        );

      if (
        !catalogResponse.ok
      ) {
        throw new Error(
          `No se pudo cargar catalog.json · HTTP ${catalogResponse.status}`
        );
      }

      catalog =
        await catalogResponse.json();

      const results =
        await Promise.all(
          arr(
            catalog.documentos
          ).map(
            async (item) => {
              try {
                const response =
                  await fetch(
                    item.ruta,
                    {
                      cache:
                        "no-store"
                    }
                  );

                if (!response.ok) {
                  throw new Error(
                    `HTTP ${response.status}`
                  );
                }

                const doc =
                  await response.json();

                if (!doc.id) {
                  doc.id =
                    item.id;
                }

                return doc;

              } catch (_) {
                return {
                  ...item,

                  estado_validacion:
                    item.estado ||
                    "NO_APROBADO",

                  fuentes_oficiales:
                    [],

                  subtemas:
                    [],

                  anexos_prioritarios:
                    []
                };
              }
            }
          )
        );

      documents =
        results.filter(Boolean);

      activeDocument =
        documents[0] ||
        null;

      renderHeader();
      renderQuickTerms();
      renderMetadata();
      renderLearning();

    } catch (error) {
      $("libraryStatus").textContent =
        "Biblioteca no disponible";

      $("libraryStatus").className =
        "status-badge warn";

      $("result").innerHTML = `
        <div class="empty-state">

          <strong>
            Error de catálogo
          </strong>

          <p>
            ${esc(
              error.message
            )}
          </p>

        </div>
      `;
    }

    checkBackend();
  }

  function init() {
    document
      .querySelectorAll(
        ".nav-btn"
      )
      .forEach(
        (button) => {
          button.addEventListener(
            "click",
            () => {
              switchView(
                button.dataset.view
              );
            }
          );
        }
      );

    $("searchForm")
      .addEventListener(
        "submit",
        (event) => {
          event.preventDefault();

          runSearch(
            $("search").value
          );
        }
      );

    $("queryForm")
      .addEventListener(
        "submit",
        (event) => {
          event.preventDefault();

          const query =
            $("q")
              .value
              .trim()
              .slice(
                0,
                CONFIG
                  .MAX_QUERY_LENGTH ||
                1200
              );

          if (!query) {
            return;
          }

          $("q").value =
            "";

          assistantQuery(
            query
          );
        }
      );

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
