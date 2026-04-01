import json
import os

PATH_DB = "/home/admin_jarvis/jarvis/config_cameras.json"

def obtenir_nom_piece(mac_adresse):
    if not os.path.exists(PATH_DB):
        return "Zone Inconnue"
    
    with open(PATH_DB, 'r') as f:
        db = json.load(f)
    
    # On cherche l'adresse MAC (en majuscules pour éviter les erreurs)
    config = db.get(mac_adresse.upper())
    if config:
        return config['piece']
    return "Zone Non Répertoriée"
