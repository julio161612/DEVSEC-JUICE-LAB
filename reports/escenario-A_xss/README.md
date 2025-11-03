# Escenario A — XSS reflexivo (evidencias)

**Objetivo:** Detectar y documentar un XSS reflexivo en OWASP Juice Shop usando OWASP ZAP (DAST) y evidencias forenses (logs y pcap).

## Resumen breve
- Se ejecutó OWASP ZAP (baseline/active scan) contra Juice Shop (http://localhost:3000).
- Se generaron reportes `zap_report.html` y `zap_report.json`.
- Se capturaron evidencias: logs y (opcional) pcap.
- Carpeta: `reports/escenario-A_xss/`

## Evidencias (capturas)

![01 Punto de escucha](images/01_listen.jpeg)
**Leyenda:** Punto de escucha y contexto del entorno (puertos/containers).

![02 Ejecución DAST en Actions](images/02_actions_run_dast.jpeg)
**Leyenda:** Ejecución del job DAST en GitHub Actions (si fue ejecutado en CI).

![03 ZAP - árbol de URLs / overview](images/03.png)
**Leyenda:** Vista del árbol de URLs de ZAP o spider.

![04 Detalle alerta XSS](images/04.jpeg)
**Leyenda:** Detalle de una alerta (posible XSS), con evidence y endpoint.

![05 Logs del servidor (petición)](images/05.jpeg)
**Leyenda:** Fragmento de logs del contenedor Juice Shop con la petición sospechosa.

![06 PCAP - selección en Wireshark](images/06.png)
**Leyenda:** Paquete HTTP que contiene la petición maliciosa (evidence).

![07 ZAP report - resumen](images/07_zap_report_html.png)
**Leyenda:** Resumen del reporte ZAP (High / Medium / Low counts).

![08 JSON snippet](images/08.png)
**Leyenda:** Fragmento del `zap_report.json` con evidence y url.

![09 JSON report (otra vista)](images/09_json_report.jpeg)
**Leyenda:** Otra vista del JSON para análisis automatizado.

## Archivos incluidos
- `zap_report.html`, `zap_report.json` — reportes ZAP.
- `images/*` — capturas numeradas.
- `attack_capture.zip` — pcap comprimido (si incluido).
- `juice_logs.txt` — logs del contenedor (si añadido).

## Reproducción (comandos seguros)
```bash
# Levantar Juice Shop
docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop

# Ejecutar ZAP baseline (Linux)
docker run --rm --network host -v $(pwd)/reports/escenario-A_xss:/zap/reports ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t http://localhost:3000 -r /zap/reports/zap_report.html -J /zap/reports/zap_report.json

# Guardar logs
docker logs juice-shop > reports/escenario-A_xss/juice_logs.txt

# Capturar tráfico (opcional, en otra terminal)
sudo tcpdump -i any -w reports/escenario-A_xss/attack_capture.pcap port 3000
# Cuando termines, comprimir:
zip reports/escenario-A_xss/attack_capture.zip reports/escenario-A_xss/attack_capture.pcap
Mitigaciones recomendadas (resumen)
Escapar/encodear salidas HTML.

Implementar Content-Security-Policy (CSP).

Añadir validación y sanitización en backend.
