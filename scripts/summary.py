import json
import os

# Ruta base de reportes
REPORTS_DIR = "reports"

def load_json(file_name):
    """Carga un archivo JSON si existe."""
    path = os.path.join(REPORTS_DIR, file_name)
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ Error leyendo {file_name}")
            return None

def summarize_semgrep(data):
    if not data or "results" not in data:
        return "Semgrep: ❌ sin resultados o archivo vacío"
    count = len(data["results"])
    return f"🔍 Semgrep detectó {count} posibles vulnerabilidades."

def summarize_npm_audit(data):
    if not data or "vulnerabilities" not in data:
        return "npm audit: ❌ sin resultados o archivo vacío"
    total = sum(vuln["total"] for vuln in data["vulnerabilities"].values())
    return f"📦 npm audit detectó {total} vulnerabilidades en dependencias."

def summarize_zap(data):
    if not data or "site" not in data:
        return "ZAP: ❌ sin resultados o archivo vacío"
    alerts = data["site"][0].get("alerts", [])
    return f"🕷️ OWASP ZAP encontró {len(alerts)} vulnerabilidades dinámicas."

def main():
    print("📊 === Resumen de Seguridad DEVSEC-JUICE-LAB ===")
    print("")

    semgrep_data = load_json("semgrep-report.json")
    npm_data = load_json("npm-audit-report.json")
    zap_data = load_json("zap-report.json")

    print(summarize_semgrep(semgrep_data))
    print(summarize_npm_audit(npm_data))
    print(summarize_zap(zap_data))

    print("\n✅ Análisis completado.")

if __name__ == "__main__":
    main()
