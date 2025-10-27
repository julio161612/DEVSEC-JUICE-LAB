#!/bin/bash
# Script: run_scans.sh
# Descripción: ejecuta escaneos de seguridad (Semgrep + npm audit)
# Autor: Julio

echo "🔍 Iniciando escaneo de seguridad..."

# Crear carpeta de reportes si no existe
mkdir -p reports

# 1️⃣ Escaneo SAST con Semgrep
echo "🚨 Ejecutando Semgrep..."
semgrep --config auto --json > reports/semgrep-report.json || echo "⚠️ Semgrep terminó con advertencias."

# 2️⃣ Escaneo de dependencias con npm audit
echo "📦 Ejecutando npm audit..."
npm install --package-lock-only > /dev/null 2>&1
npm audit --json > reports/npm-audit-report.json || echo "⚠️ npm audit terminó con advertencias."

echo "✅ Escaneos completados. Revisa los reportes en la carpeta 'reports/'"
