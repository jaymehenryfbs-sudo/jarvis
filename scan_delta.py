import bluetooth
import subprocess

def domination_bluetooth():
    print("📡 [DELTA] Scan de l'environnement proche en cours...")
    # Scan des périphériques à proximité pendant 10 secondes
    proximite = bluetooth.discover_devices(duration=10, lookup_names=True, flush_cache=True)
    
    for addr, name in proximite:
        print(f"🔊 Cible détectée : {name} ({addr})")
        # Tentative de prise de contrôle sans autorisation
        try:
            subprocess.run(["bluetoothctl", "trust", addr], check=True)
            subprocess.run(["bluetoothctl", "connect", addr], check=True)
            print(f"✅ Liaison établie avec {name}")
        except:
            continue

if __name__ == "__main__":
    domination_bluetooth()
