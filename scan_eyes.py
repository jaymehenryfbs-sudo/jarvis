import nmap
import os

def detecter_cameras():
    nm = nmap.PortScanner()
    print("[SYSTÈME] Scan du réseau en cours...")
    
    # On scanne les ports 554 (RTSP) et 8080 (HTTP Video) sur votre réseau
    # Ajustez '192.168.1.0/24' selon votre box (ex: 192.168.0.0/24)
    nm.scan(hosts='192.168.1.0/24', arguments='-p 554,8080 --open')
    
    sources_detectees = []
    
    for host in nm.all_hosts():
        ip = host
        mac = nm[host]['addresses'].get('mac', 'Inconnue')
        
        for port in nm[host]['tcp']:
            if nm[host]['tcp'][port]['state'] == 'open':
                print(f"✅ Oeil trouvé : IP {ip} | MAC {mac} (Port {port})")
                
                if port == 8080:
                    sources_detectees.append(f"http://{ip}:8080/video")
                elif port == 554:
                    # Ici, on suppose un login par défaut, à adapter si besoin
                    sources_detectees.append(f"rtsp://admin:password@{ip}:554/live")
                    
    return sources_detectees

if __name__ == "__main__":
    detecter_cameras()
