(() => {
"use strict";

const CATALOG_URL="data/metadata/catalog.json";
const SERUMS_MANIFEST_URL="knowledge/minsa/serums-2026-ii/manifest.json";
const SERUMS_RAG_BASE="knowledge/minsa/serums-2026-ii/";
const API=window.SIP_API||null;
const CONFIG=window.SIP_CONFIG||{MAX_QUERY_LENGTH:1200};
let catalog=null,documents=[],activeDocument=null,serumsManifest=null;
const ragTextCache=new Map();
const $=id=>document.getElementById(id);
const arr=v=>Array.isArray(v)?v:[];
const esc=v=>String(v??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const norm=v=>String(v??"").normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase();

function statusClass(v){v=norm(v);if(v.includes("validado_oficial"))return"ok";if(v.includes("no_aprobado"))return"warn";return"pending";}
function officialSources(doc){return arr(doc?.fuentes_oficiales);}
function officialUrl(doc){return doc?.url_oficial||officialSources(doc).find(s=>s?.url)?.url||"";}
function documentLabel(doc){return doc?.numero_norma||doc?.resolucion_aprobatoria||doc?.titulo||doc?.id||"Documento";}
function switchView(name){document.querySelectorAll(".view").forEach(v=>v.classList.toggle("active",v.id===`view-${name}`));document.querySelectorAll(".nav-btn").forEach(b=>b.classList.toggle("active",b.dataset.view===name));}
function renderHeader(){const total=serumsManifest?.documentos_unicos||documents.length;$("sourceCount").textContent=total;$("annexCount").textContent=documents.reduce((n,d)=>n+arr(d?.anexos_prioritarios).length,0);$("validationState").textContent=total?"BIBLIOTECA SERUMS":"—";const s=$("libraryStatus");s.textContent=total?`Biblioteca SERUMS · ${total} documentos · ${serumsManifest?.compendios_descubiertos||17} compendios`:"Biblioteca no disponible";s.className=total?"status-badge":"status-badge warn";}
function renderQuickTerms(){const terms=[...new Set(documents.flatMap(d=>[d.tema,d.bloque_SERUMS,...arr(d.subtemas),...arr(d.compendios_origen)]).filter(Boolean))].filter(t=>!/^ver las? \d+ normas?$/i.test(String(t))).slice(0,16);$("quickTerms").innerHTML=terms.map(t=>`<button class="chip" type="button" data-query="${esc(t)}">${esc(t)}</button>`).join("");$("quickTerms").querySelectorAll(".chip").forEach(b=>b.addEventListener("click",()=>{$("search").value=b.dataset.query;runSearch(b.dataset.query);}));}

function renderMetadata(){
 if(!activeDocument){$("metadata").innerHTML='<div class="empty-state"><strong>Sin documento activo</strong></div>';return;}
 const mods=arr(activeDocument?.vigencia?.modificatorias),annexes=arr(activeDocument?.anexos_prioritarios),sources=officialSources(activeDocument),isCorpus=activeDocument._serumsCorpus;
 $("metadata").innerHTML=`<div style="display:flex;gap:12px;align-items:center;justify-content:space-between;flex-wrap:wrap;margin-bottom:16px"><div><span class="eyebrow">Documento activo</span><h3 style="margin:.25rem 0 0">${esc(documentLabel(activeDocument))}</h3></div><select id="documentSelector" aria-label="Seleccionar documento">${documents.map(doc=>`<option value="${esc(doc.id)}" ${doc.id===activeDocument.id?"selected":""}>${esc(documentLabel(doc))}</option>`).join("")}</select></div>
 <div class="metadata-grid"><article class="meta-card"><span class="eyebrow">Documento</span><h3>${esc(activeDocument.titulo||documentLabel(activeDocument))}</h3><p>${esc(activeDocument.tema||"Bibliografía oficial SERUMS 2026-II")}</p></article><article class="meta-card"><span class="eyebrow">Estado documental</span><h3>${esc(activeDocument.estado_validacion||"No registrado")}</h3><p>${isCorpus?(activeDocument.archivo_rag?`Texto materializado para RAG${activeDocument.metodo_extraccion?` · ${esc(activeDocument.metodo_extraccion)}`:""}.`:"Documento oficial identificado; texto pendiente de extracción."):(mods.length?mods.map(x=>`${esc(x.resolucion)} · ${esc(x.alcance||"")}`).join("<br>"):"Sin modificatorias cargadas.")}</p></article><article class="meta-card"><span class="eyebrow">Origen</span><h3>${esc(isCorpus?"SERUMS 2026-II":activeDocument.bloque_SERUMS||"Biblioteca SIP")}</h3><p>${esc(arr(activeDocument.compendios_origen).join(" · ")||activeDocument.alcance_profesional||"")}</p></article></div>
 <div class="trace"><b>Trazabilidad:</b> documento oficial → página/sección → conocimiento → resultado de búsqueda → fuente original.</div>
 <div class="metadata-grid">${annexes.map(i=>`<article class="meta-card"><span class="tag ${statusClass(i.estado_validacion)}">${esc(i.estado_validacion)}</span><h3>${esc(i.anexo)} · ${esc(i.nombre)}</h3><p>${esc(i.nota||"")}</p></article>`).join("")}${sources.map(s=>`<article class="meta-card"><span class="tag ${statusClass(s.estado_validacion)}">${esc(s.estado_validacion)}</span><h3>${esc(s.documento)}</h3><p>${esc(s.rol_evidencia||"Fuente oficial")}</p>${s.url?`<a class="source-link" href="${esc(s.url)}" target="_blank" rel="noopener">Abrir fuente oficial ↗</a>`:""}</article>`).join("")}${isCorpus&&activeDocument.url_oficial?`<article class="meta-card"><span class="tag ${statusClass(activeDocument.estado_validacion)}">${esc(activeDocument.estado_validacion)}</span><h3>Fuente oficial MINSA</h3><p>${activeDocument.archivo_rag?"Documento incorporado al corpus RAG.":"Extracción de texto pendiente."}</p><a class="source-link" href="${esc(activeDocument.url_oficial)}" target="_blank" rel="noopener">Abrir fuente oficial ↗</a>${activeDocument.pdf_oficial?` <a class="source-link" href="${esc(activeDocument.pdf_oficial)}" target="_blank" rel="noopener">PDF oficial ↗</a>`:""}</article>`:""}</div>`;
 $("documentSelector")?.addEventListener("change",event=>selectDocument(event.target.value));
}
function renderLearning(){const resources=documents.flatMap(d=>Object.values(d.recursos_pedagogicos||{}).map(r=>({...r,document:documentLabel(d)})));$("learningResources").innerHTML=resources.length?`<div class="resource-grid">${resources.map(r=>`<article class="resource-card"><span class="tag ${statusClass(r.estado)}">${esc(r.estado)}</span><h3>${esc(r.titulo)}</h3><p><b>${esc(r.document)}</b> · ${esc(r.id)}</p><p>${esc(r.motivo||"")}</p></article>`).join("")}</div>`:'<div class="empty-state"><strong>Sin recursos pedagógicos cargados</strong></div>';}

function normalizedSearchText(value){return norm(value).replace(/resolucion ministerial/g,"rm").replace(/decreto supremo/g,"ds").replace(/decreto legislativo/g,"dl").replace(/norma tecnica de salud/g,"nts").replace(/\bn\s*[.°ºo]*\s*/g," ").replace(/[^a-z0-9]+/g," ").replace(/\s+/g," ").trim();}
function normativeIdentifier(value){const v=normalizedSearchText(value);const m=v.match(/\b(nts|rm|ds|dl|ley)\s+(\d{1,5})(?:\s+(\d{4}))?\b/);return m?{type:m[1],number:m[2],year:m[3]||""}:null;}
function classifyDocument(doc){
 const h=normalizedSearchText(`${doc.titulo||""} ${doc.texto_indice||""} ${doc._ragText||""}`);
 const defs=[["NTS",/\bnts\s+\d+/],["LEY",/\bley\s+\d+/],["RM",/\brm\s+\d+/],["DS",/\bds\s+\d+/],["DL",/\bdl\s+\d+/],["DIRECTIVA",/\bdirectiva\b/],["GUIA",/\bguia\b|\bgpc\b/],["DOCUMENTO TECNICO",/\bdocumento tecnico\b/],["ANEXO",/\banexo\b/]];
 return defs.find(([,rx])=>rx.test(h))?.[0]||"OTROS";
}
function documentSearchText(doc){return [doc.id,doc.titulo,doc.numero_norma,doc.resolucion_aprobatoria,doc.texto_indice,doc.tema,doc.bloque_SERUMS,doc.institucion,doc.tipo,doc.tipo_fuente,doc._ragText,...arr(doc.subtemas),...arr(doc.compendios_origen),...arr(doc.compendios_urls)].filter(Boolean).join(" ");}
function pageForIndex(text,index){const before=text.slice(0,index);const matches=[...before.matchAll(/\[\[PAGINA\s+(\d+)\]\]/gi)];return matches.length?matches[matches.length-1][1]:"";}
function snippetFor(doc,query){
 const raw=doc._ragText||"";if(!raw)return doc.archivo_rag?"Contenido RAG cargado sin coincidencia contextual.":"Documento oficial identificado; extracción de texto pendiente.";
 const q=normalizedSearchText(query);const terms=q.split(/\s+/).filter(t=>t.length>1);const lower=norm(raw);let idx=-1;
 for(const t of terms){idx=lower.indexOf(t);if(idx>=0)break;}
 if(idx<0)return "Coincidencia en metadatos documentales.";
 const start=Math.max(0,idx-140),end=Math.min(raw.length,idx+260),page=pageForIndex(raw,idx);
 const excerpt=raw.slice(start,end).replace(/\[\[PAGINA\s+\d+\]\]/gi," ").replace(/\s+/g," ").trim();
 return `${page?`Página ${page} · `:""}…${excerpt}…`;
}
function searchableRecords(){return documents.flatMap(doc=>[{type:doc._serumsCorpus?classifyDocument(doc):"Documento",title:documentLabel(doc),text:documentSearchText(doc),state:doc.estado_validacion,detail:doc.titulo||documentLabel(doc),url:officialUrl(doc),docId:doc.id,doc},...arr(doc?.vigencia?.modificatorias).map(i=>({type:"Modificatoria",title:i.resolucion,text:`${i.resolucion} ${i.alcance||""}`,state:"VALIDADO_OFICIAL",detail:i.alcance||"",url:officialSources(doc).find(s=>s.documento===i.resolucion)?.url||officialUrl(doc),docId:doc.id,doc})),...arr(doc?.anexos_prioritarios).map(i=>({type:"Anexo",title:`${i.anexo} · ${i.nombre}`,text:`${i.anexo} ${i.nombre} ${i.nota||""}`,state:i.estado_validacion,detail:i.nota||"",url:officialUrl(doc),docId:doc.id,doc}))]);}
function searchRecords(query){
 const q=normalizedSearchText(query),terms=q.split(/\s+/).filter(Boolean);if(!terms.length)return[];
 const requestedId=normativeIdentifier(query);
 return searchableRecords().map(r=>{const h=normalizedSearchText(`${r.title} ${r.text} ${r.detail}`);
  if(requestedId){const pattern=new RegExp(`\\b${requestedId.type}\\s+${requestedId.number}${requestedId.year?`\\s+${requestedId.year}`:""}\\b`);if(!pattern.test(h))return{...r,score:0};return{...r,score:100+terms.filter(t=>h.includes(t)).length,detail:snippetFor(r.doc,query)};}
  const matched=terms.filter(t=>h.includes(t)).length;if(!matched)return{...r,score:0};
  const coverage=matched/terms.length;const titleHit=terms.filter(t=>normalizedSearchText(r.title).includes(t)).length;
  return{...r,score:(coverage*10)+titleHit,detail:snippetFor(r.doc,query)};
 }).filter(r=>r.score>0).sort((a,b)=>b.score-a.score);
}
function resultHtml(records,query){if(!records.length)return`<div class="empty-state"><strong>EVIDENCIA_INSUFICIENTE</strong><p>No hay coincidencia documental para “${esc(query)}” en la biblioteca cargada.</p></div>`;return records.slice(0,100).map(r=>`<article class="evidence-card"><div class="tag-row"><span class="tag">${esc(r.type)}</span><span class="tag ${statusClass(r.state)}">${esc(r.state)}</span></div><h3>${esc(r.title)}</h3><p>${esc(r.detail)}</p><button type="button" class="open-result-doc" data-id="${esc(r.docId)}">Abrir documento</button>${r.url?`<a class="source-link" href="${esc(r.url)}" target="_blank" rel="noopener">Fuente oficial ↗</a>`:""}</article>`).join("");}
function bindResultButtons(){document.querySelectorAll(".open-result-doc").forEach(b=>b.addEventListener("click",()=>{selectDocument(b.dataset.id);switchView("source");}));}
function runSearch(query){const v=String(query||"").trim();$("result").className="results";$("result").innerHTML=v?resultHtml(searchRecords(v),v):'<div class="empty-state"><strong>Escribe una consulta</strong></div>';bindResultButtons();}
function selectDocument(id){activeDocument=documents.find(d=>d.id===id)||documents[0]||null;renderMetadata();}

async function loadRagTexts(corpus){
 const queue=corpus.filter(d=>d.archivo_rag);let cursor=0;const workers=Math.min(6,queue.length);
 async function worker(){while(cursor<queue.length){const d=queue[cursor++];if(ragTextCache.has(d.archivo_rag)){d._ragText=ragTextCache.get(d.archivo_rag);continue;}try{const r=await fetch(`${SERUMS_RAG_BASE}${encodeURIComponent(d.archivo_rag)}`,{cache:"force-cache"});if(r.ok){const text=await r.text();ragTextCache.set(d.archivo_rag,text);d._ragText=text;}}catch(e){console.warn("RAG no disponible",d.archivo_rag,e);}}}
 await Promise.all(Array.from({length:workers},worker));
}
function renderNormExplorer(){
 const panel=document.querySelector("#view-explore .search-panel");if(!panel||$("normExplorer"))return;
 const box=document.createElement("details");box.id="normExplorer";box.className="document-types";box.innerHTML='<summary><span><strong>Explorar por tipo de norma</strong><small>Leyes · NTS · RM · DS · DL · Directivas · Guías · Documentos técnicos</small></span><span aria-hidden="true">⌄</span></summary><div id="normTypeButtons" class="document-type-grid"></div><div id="normTypeList" class="results"></div>';
 panel.insertBefore(box,$("result"));
 const counts={};documents.filter(d=>d._serumsCorpus).forEach(d=>{const t=classifyDocument(d);counts[t]=(counts[t]||0)+1;});
 $("normTypeButtons").innerHTML=Object.entries(counts).sort((a,b)=>a[0].localeCompare(b[0])).map(([t,n])=>`<button type="button" class="doc-type-filter" data-norm-type="${esc(t)}">${esc(t)} · ${n}</button>`).join("");
 $("normTypeButtons").querySelectorAll("button").forEach(b=>b.addEventListener("click",()=>renderNormList(b.dataset.normType)));
}
function renderNormList(type){
 const list=documents.filter(d=>d._serumsCorpus&&classifyDocument(d)===type).sort((a,b)=>documentLabel(a).localeCompare(documentLabel(b),"es"));
 $("normTypeList").innerHTML=list.map(d=>`<article class="evidence-card"><div class="tag-row"><span class="tag">${esc(type)}</span><span class="tag ${statusClass(d.estado_validacion)}">${esc(d.estado_validacion)}</span></div><h3>${esc(documentLabel(d))}</h3><p>${esc(d.titulo||"")}</p><button type="button" class="norm-search" data-id="${esc(d.id)}">Buscar esta norma</button>${officialUrl(d)?`<a class="source-link" href="${esc(officialUrl(d))}" target="_blank" rel="noopener">Fuente oficial ↗</a>`:""}</article>`).join("");
 $("normTypeList").querySelectorAll(".norm-search").forEach(b=>b.addEventListener("click",()=>{const d=documents.find(x=>x.id===b.dataset.id);if(!d)return;$("search").value=documentLabel(d);runSearch(documentLabel(d));}));
}

function addMessage(role,title,text){const c=document.createElement("div");c.className=`message ${role}`;c.innerHTML=`<span class="avatar">${role==="user"?"TÚ":"SIP"}</span><div><strong>${esc(title)}</strong><p>${esc(text)}</p></div>`;$("out").appendChild(c);c.scrollIntoView({behavior:"smooth",block:"nearest"});}
async function assistantQuery(message){addMessage("user","Consulta",message);const local=searchRecords(message);if(local.length){addMessage("system","Evidencia documental",local.slice(0,5).map(r=>`${r.type}: ${r.title} — ${r.detail}`).join("\n\n"));return;}if(!API?.chat||!window.SIP_CONFIG?.API_BASE_URL){addMessage("system","EVIDENCIA_INSUFICIENTE","La biblioteca local no contiene evidencia suficiente y el backend RAG aún no está desplegado.");return;}try{const response=await API.chat(message);addMessage("system","Respuesta RAG",response?.answer||"El backend respondió sin contenido.");}catch(e){addMessage("system","Backend no disponible",e.message);}}
async function checkBackend(){const b=$("backendStatus");if(!API?.health||!window.SIP_CONFIG?.API_BASE_URL){b.textContent="Backend pendiente";b.className="mini-status warn";return;}try{const h=await API.health();b.textContent=h?.rag_active?"RAG activo":"API activa · RAG sin índice";b.className="mini-status";}catch(_){b.textContent="Backend no disponible";b.className="mini-status warn";}}

async function loadLibrary(){
 try{
  const [catalogResponse,manifestResponse]=await Promise.all([fetch(CATALOG_URL,{cache:"no-store"}),fetch(SERUMS_MANIFEST_URL,{cache:"no-store"})]);
  if(!catalogResponse.ok)throw new Error(`No se pudo cargar catalog.json · HTTP ${catalogResponse.status}`);
  catalog=await catalogResponse.json();if(manifestResponse.ok)serumsManifest=await manifestResponse.json();
  const base=await Promise.all(arr(catalog.documentos).map(async item=>{try{const r=await fetch(item.ruta,{cache:"no-store"});if(!r.ok)throw new Error();const d=await r.json();if(!d.id)d.id=item.id;return d;}catch(_){return{...item,estado_validacion:item.estado||"NO_APROBADO",fuentes_oficiales:[],subtemas:[],anexos_prioritarios:[]};}}));
  const corpus=arr(serumsManifest?.documentos).map(d=>({...d,_serumsCorpus:true,institucion:"Ministerio de Salud del Perú",tema:"Bibliografía oficial SERUMS 2026-II",bloque_SERUMS:"SERUMS 2026-II",fuentes_oficiales:d.url_oficial?[{documento:d.titulo||d.id,url:d.url_oficial,estado_validacion:d.estado_validacion,rol_evidencia:"Fuente oficial MINSA"}]:[],subtemas:[],anexos_prioritarios:[]}));
  await loadRagTexts(corpus);
  const map=new Map();[...base.filter(Boolean),...corpus].forEach(d=>{const key=d.url_oficial||officialUrl(d)||d.id;if(!map.has(key))map.set(key,d);});
  documents=[...map.values()];activeDocument=documents[0]||null;
  renderHeader();renderQuickTerms();renderMetadata();renderLearning();renderNormExplorer();
 }catch(e){$("libraryStatus").textContent="Biblioteca no disponible";$("libraryStatus").className="status-badge warn";$("result").innerHTML=`<div class="empty-state"><strong>Error de catálogo</strong><p>${esc(e.message)}</p></div>`;}
 checkBackend();
}
function init(){document.querySelectorAll(".nav-btn").forEach(b=>b.addEventListener("click",()=>switchView(b.dataset.view)));$("searchForm").addEventListener("submit",e=>{e.preventDefault();runSearch($("search").value);});$("queryForm").addEventListener("submit",e=>{e.preventDefault();const q=$("q").value.trim().slice(0,CONFIG.MAX_QUERY_LENGTH||1200);if(!q)return;$("q").value="";assistantQuery(q);});loadLibrary();}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
})();
