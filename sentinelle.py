import face_recognition
import cv2
import requests
from auto_config import scan_autonome
from voix import parler

# Configuration Telegram
TOKEN = "VOTRE_TOKEN"
CHAT_ID = "VOTRE_ID"

print("[SYSTÈME] J.A.R.V.I.S. synchronise les caméras...")
db = scan_autonome()

# Chargement Monsieur
img_ref = face_recognition.load_image_file("/home/admin_jarvis/jarvis/visages_connus/monsieur.jpg")
encodage_monsieur = face_recognition.face_encodings(img_ref)[0]
if match[0]:
    print("Monsieur reconnu.")
    parler("Ravi de vous voir, Monsieur. Sécurité confirmée.")
else:
    print("INTRUS DÉTECTÉ !")
    parler("Alerte ! Individu non identifié. Quittez la zone immédiatement.")
    # Le reste du code (envoi Telegram, etc.) continue ici...

sources = []
for mac, info in db.items():
    # On récupère l'IP peu importe si elle s'appelle 'ip' ou 'ip_actuelle'
    ip_detectee = info.get('ip') or info.get('ip_actuelle')
    type_cam = info.get('type', 'RTSP')
    
    if ip_detectee:
        if type_cam == "RTSP":
            url = f"rtsp://admin:password@{ip_detectee}:554/live"
        else:
            url = f"http://{ip_detectee}:8080/video"
        sources.append((cv2.VideoCapture(url), info.get('piece', 'Zone Inconnue')))
print(f"[SYSTÈME] Surveillance active sur {len(sources)} zones.")

while True:
    for cap, piece in sources:
        ret, frame = cap.read()
        if not ret: continue
        
        # Analyse rapide
        small = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
        rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)
        
        for enc in face_recognition.face_encodings(rgb):
            if not face_recognition.compare_faces([encodage_monsieur], enc)[0]:
                # ALERTE
                cv2.imwrite("/tmp/intrus.jpg", frame)
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", 
                              data={'chat_id': CHAT_ID, 'caption': f"🚨 INTRUS détecté : {piece}"},
                              files={'photo': open("/tmp/intrus.jpg", 'rb')})
