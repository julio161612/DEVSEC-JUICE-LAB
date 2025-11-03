# 🧠 DEVSEC JUICE LAB

**Proyecto práctico de ciberseguridad DevSecOps** creado por [@julio161612](https://github.com/julio161612).  
Este laboratorio combina **OWASP Juice Shop** con un pipeline de análisis de seguridad automatizado (SAST, DAST y Dependency Scanning).

---

## 🎯 Objetivos del Proyecto

- Aprender los fundamentos de **DevSecOps** (Integración de seguridad en el ciclo de vida del software).
- Montar un entorno de pruebas local con **Docker y OWASP Juice Shop**.
- Implementar un pipeline de seguridad usando **GitHub Actions** con:
  - **Semgrep** (SAST)
  - **OWASP ZAP** (DAST)
  - **npm audit** (análisis de dependencias)
- Crear reportes automáticos de vulnerabilidades.
- Documentar cada etapa del proceso para portafolio profesional.

---

## 🏗️ Estructura del Repositorio
DEVSEC-JUICE-LAB/
├─ .github/workflows/ → Workflows CI/CD de seguridad
├─ reports/ → Reportes generados (ZAP, Semgrep, etc.)
├─ demos/ → Capturas, GIFs o vídeos de demostración
├─ scripts/ → Scripts utilitarios
├─ README.md → Documentación principal
└─ .gitignore → Archivos ignorados por Git

---

## Entorno y Montaje de OWASP Juice Shop

1. Asegúrate de tener Docker instalado:
   ```bash
   docker --version
2. Levanta Juice Shop en un contenedor:

docker run --rm -d -p 3000:3000 --name juice-shop bkimminich/juice-shop:latest
3. Comprueba que funciona abriendo:

http://localhost:3000
4. Para detener el contenedor:

docker stop juice-shop

💡 Consejos
No ejecutes OWASP Juice Shop en entornos públicos o de producción.

Usa este laboratorio como práctica personal o para mostrar tus habilidades.

## Resumen del proyecto

DEVSEC-JUICE-LAB es un pipeline DevSecOps reproducible que automatiza SAST (Semgrep/CodeQL), análisis de dependencias (npm audit) y DAST (OWASP ZAP) contra una aplicación vulnerable (Juice Shop), generando reportes y artefactos para triage.
Se integra en GitHub Actions para ejecuciones automáticas en cada push/PR y produce evidencia (JSON/HTML/pcap/logs) lista para auditoría.


## Reproducible en empresas — cómo y por qué

Contenedores y compose: Juice Shop y ZAP se ejecutan en Docker (o Docker Compose), garantizando que cualquier equipo pueda levantar la misma versión de la app y escáneres en poco tiempo.

Automatización y artefactos: los workflows producen artefactos y alertas (reportes JSON/HTML, resumen en logs) que encajan con procesos corporativos de triage (crear tickets, asignar remediaciones), facilitando integración con ticketing/Slack/SIEM.

## Escalabilidad

Herramientas y paralelización: convertir jobs en ejecuciones paralelas (por servicio/por microservicio) y añadir escáneres adicionales (SCA, secret scanners, container scanners).

SIEM: enviar logs/reportes a ELK/OpenSearch, Wazuh o Splunk para correlación y alertas centralizadas, y orquestar respuestas (crear issues, abrir PRs) automáticamente.

Políticas y gating: añadir gates de política y dashboards para gestión de riesgo en escala.


📬 Autor
Julio — Estudiante de Ciberseguridad
GitHub: @julio161612
