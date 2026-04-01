# ~/jarvis/deploy_jarvis.py
import os
import subprocess
import time

TARGET_IP = "192.168.0.71:32961"
APK_NAME = "JARVIS_Interface.apk"
DOWNLOAD_PATH = os.path.expanduser("~/Downloads/")

def deploy():
    print(f"[SURVEILLANCE] En attente de l'APK dans {DOWNLOAD_PATH}...")
    
    while True:
        if os.path.exists(DOWNLOAD_PATH + APK_NAME):
            print(f"[DÉTECTION] APK trouvé. Initialisation du transfert vers {TARGET_IP}...")
            
            # Connexion et installation via le pont ADB déjà établi
            try:
                subprocess.run(["adb", "-s", TARGET_IP, "install", "-r", DOWNLOAD_PATH + APK_NAME], check=True)
                print("[SUCCÈS] Installation terminée.")
                
                # Lancement automatique de l'interface
                subprocess.run(["adb", "-s", TARGET_IP, "shell", "monkey", "-p", "org.test.jarvis", "-c", "android.intent.category.LAUNCHER", "1"])
                print("[SYSTÈME] Interface TC.01 lancée.")
                break
            except Exception as e:
                print(f"[ERREUR] Échec du déploiement : {e}")
                break
        time.sleep(10)

if __name__ == "__main__":
    deploy()
