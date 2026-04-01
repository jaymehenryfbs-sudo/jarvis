# ~/jarvis/auto_config.py
import subprocess
import json
import os

def obtenir_ip_tailscale():
    try:
        # Extraction de l'adresse du tunnel via le CLI Tailscale
        result = subprocess.check_output(["tailscale", "ip", "-4"]).decode("utf-8").strip()
        return result
    except:
        return "127.0.0.1"

def lier_interface_au_cerveau():
    ip = obtenir_ip_tailscale()
    url_cerveau = f"http://{ip}:5000"
    
    config = {
        "cerveau_url": url_cerveau,
        "mode": "delta",
        "version": "1.0.2"
    }
    
    # Injection dans le dossier de l'interface pour la prochaine forge
    config_path = os.path.expanduser("~/jarvis/interface/config_jarvis.json")
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)
    
    print(f"[SYSTEME] Liaison établie : {url_cerveau}")
    return url_cerveau

if __name__ == "__main__":
    lier_interface_au_cerveau()
