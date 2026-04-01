from gtts import gTTS
import os

def dire(texte):
    if not texte: return
    # Création du fichier audio temporaire
    tts = gTTS(text=texte, lang='fr')
    tts.save("voix.mp3")
    # Lecture via le matériel audio de l'ordinateur
    os.system("mpg123 -q voix.mp3")
