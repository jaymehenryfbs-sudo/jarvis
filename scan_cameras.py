import nmap
import os

def scanner_reseau():
    nm = nmap.PortScanner()
    print("[SYSTÈME] Scan du réseau en cours (Recherche de caméras)...")
    # Remplacez 192.168.1.0/24 par la plage de votre box
    nm.scan(hosts='192.168.1.0/24', arguments='-p 554,8080 --open')
    
    cameras_trouvees = []
    for host in nm.all_hosts():
        ip = host
        mac = nm[host]['addresses'].get('mac', 'Inconnue')
        nom = nm[host].hostname()
        
        for port in nm[host]['tcp']:
            if nm[host]['tcp'][port]['state'] == 'open':
                print(f"📷 Caméra potentielle trouvée : {ip} (MAC: {mac})")
                if port == 8080:
                    cameras_trouvees.append(f"http://{ip}:8080/video")
                else:
                    # Note : Le mot de passe devra être ajouté manuellement dans sentinelle.py
                    cameras_trouvees.append(f"rtsp://admin:password@{ip}:554/stream1")
    
    return cameras_trouvees

if __name__ == "__main__":
    urls = scanner_reseau()
    print(f"\n[RÉSULTAT] {len(urls)} sources détectées.")
