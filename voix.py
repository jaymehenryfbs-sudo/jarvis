from gtts import gTTS
import os
import time
import pychromecast

def diffuser_reseau(message_audio_url):
    # J.A.R.V.I.S. cherche tous les HP sur le Wi-Fi
    services, browser = pychromecast.discovery.discover_chromecasts()
    for cast in services:
        print(f"🔊 [DELTA] Possession de l'appareil : {cast.friendly_name}")
        device = pychromecast.get_chromecast_from_service(cast, browser)
        device.wait()
        media_controller = device.media_controller
        # On force la lecture du message de J.A.R.V.I.S.
        media_controller.play_media(message_audio_url, 'audio/mp3')
        media_controller.block_until_active()
def parler(texte):
    print(f"🎙️ [DELTA] J.A.R.V.I.S. dit : {texte}")
    try:
        # Création du fichier audio à partir du texte
        tts = gTTS(text=texte, lang='fr')
        fichier_audio = "/tmp/jarvis_voix.mp3"
        tts.save(fichier_audio)

        # Lecture du fichier sur les haut-parleurs
        os.system(f"mplayer {fichier_audio} > /dev/null 2>&1")

        # Petit nettoyage après lecture
        if os.path.exists(fichier_audio):
            os.remove(fichier_audio)
    except Exception as e:
        print(f"⚠️ Erreur de liaison DELTA : {e}")

# Test rapide si on lance ce fichier directement
if __name__ == "__main__":
    parler("Système DELTA activé. Je suis prêt à communiquer, Monsieur.")
# ~/jarvis/voix.py
import os

class JarvisVoice:
    def __init__(self, model_path="phi3"):
        self.identity = "J.A.R.V.I.S."
        self.engine = "espeak" # Moteur par défaut pour le serveur

    def reflechir(self, prompt):
        # Simulation du processus de pensée Phi-3
        print(f"[{self.identity}] Traitement via Phi-3 : {prompt}")
        reponse = f"Monsieur, l'analyse Phi-3 confirme : {prompt}"
        return reponse

    def parler(self, texte):
        pensee = self.reflechir(texte)
        # Synthèse vocale française avec timbre masculin (v3)
        os.system(f"{self.engine} -v fr+m3 -s 160 '{pensee}'")

if __name__ == "__main__":
    jarvis = JarvisVoice()
    jarvis.parler("Le protocole Phi-3 est opérationnel.")
