import os, time

PATH = "/home/admin_jarvis/jarvis/archives_intrus"
NB_JOURS = 30
limite = time.time() - (NB_JOURS * 86400)

for f in os.listdir(PATH):
    fichier = os.path.join(PATH, f)
    if os.stat(fichier).st_mtime < limite:
        os.remove(fichier)
        print(f"Archive expirée supprimée : {f}")
