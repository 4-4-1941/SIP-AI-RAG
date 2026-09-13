from datetime import datetime,timezone
from rag.ingestion.el_peruano_sync import classify,build,duplicate,discover_from_listing
def test_clasificacion():
 assert classify("Servicio Rural y Urbano Marginal de Salud SERUMS")=="confirmada"
 assert classify("DIGEP plazas remuneradas para profesionales de la salud")=="pendiente"
 assert classify("campaña de vacunación")=="descartada"
def test_72h():
 n=build("https://www.gob.pe/institucion/minsa/normas-legales/1","<h1>Resolución Ministerial 617-2026-MINSA</h1><p>Servicio Rural y Urbano Marginal de Salud SERUMS</p>",datetime(2026,9,13,tzinfo=timezone.utc))
 assert (datetime.fromisoformat(n.visible_hasta)-datetime.fromisoformat(n.fecha_incorporacion)).total_seconds()==259200
def test_dedupe_tres_claves():
 r={"normas":[{"url_oficial":"https://www.gob.pe/x","numero_norma":"617-2026-MINSA","hash_documento":"abc"}]}
 assert duplicate({"url_oficial":"https://www.gob.pe/x/","numero_norma":"","hash_documento":""},r)
 assert duplicate({"url_oficial":"","numero_norma":"617-2026-MINSA","hash_documento":""},r)
 assert duplicate({"url_oficial":"","numero_norma":"","hash_documento":"abc"},r)
def test_descubrimiento_lista_oficial():
 h='<a href="/institucion/minsa/normas-legales/123-rm">Resolución</a><a href="/institucion/otra/normas-legales/9">No</a>'
 assert discover_from_listing(h)==[("https://www.gob.pe/institucion/minsa/normas-legales/123-rm","Resolución")]
def test_rm_617_confirmada():
 h="<h1>Resolución Ministerial N.° 617-2026-MINSA</h1><p>Modificar artículos del Reglamento de la Ley N° 23330, Ley del Servicio Rural y Urbano Marginal de Salud - SERUMS</p>"
 n=build("https://www.gob.pe/institucion/minsa/normas-legales/617",h,datetime(2026,9,13,tzinfo=timezone.utc))
 assert n.relacion_serums=="confirmada" and n.numero_norma=="617-2026-MINSA"
