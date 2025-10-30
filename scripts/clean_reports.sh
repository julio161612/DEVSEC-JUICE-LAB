#!/bin/bash

echo "🧹 Limpiando reportes antiguos..."

# Elimina todo el contenido de la carpeta reports, pero no la carpeta
rm -rf reports/*
mkdir -p reports

echo "✅ Directorio limpio. Listo para generar nuevos reportes."
