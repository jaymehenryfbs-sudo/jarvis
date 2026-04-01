from google import genai
import requests
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "online", "system": "J.A.R.V.I.S. Core"}), 200
# CONFIGURATION SATELLITE GEMINI (SDK 2026)
client = genai.Client(api_key="VOTRE_CLE_API_ICI")
MODEL_ID = "gemini-1.5-flash"

@app.route('/command', methods=['POST'])
def command():
    user_input = request.json.get("text")
    if not user_input:
        return jsonify({"response": "Monsieur ?"}), 400
    
    # TENTATIVE 1 : GEMINI CLOUD
    try:
        # Correction de la syntaxe TypeError : on utilise 'message='
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=user_input
        )
        return jsonify({"response": response.text})
        
    except Exception as e:
        print(f"Erreur Cloud : {e}")
        # TENTATIVE 2 : NOYAU LOCAL
        try:
            res = requests.post(
                "http://localhost:11434/api/generate", 
                json={"model": "phi3", "prompt": user_input, "stream": False},
                timeout=10
            )
            return jsonify({"response": "[LOCAL] " + res.json()['response']})
        except:
            return jsonify({"response": "Systèmes de réflexion hors ligne."})        
        # TENTATIVE 2 : NOYAU LOCAL (OLLAMA / PHI-3)
        try:
            res = requests.post(
                "http://localhost:11434/api/generate", 
                json={
                    "model": "phi3", 
                    "prompt": user_input, 
                    "stream": False
                },
                timeout=10
            )
            return jsonify({"response": "[LOCAL] " + res.json()['response']})
        except Exception as local_e:
            print(f"Noyau local indisponible: {local_e}")
            return jsonify({"response": "Monsieur, tous mes systèmes de réflexion sont hors ligne."})

if __name__ == "__main__":
    # Stockage de sécurité sur vos 947 Go
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# --- ROUTE RACINE (Correctif 404 pour l'APK) ---
@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "online", "message": "J.A.R.V.I.S. Operationnel"}), 200

# --- ROUTE DES COMMANDES ---
@app.route('/commande', methods=['POST'])
def commande():
    data = request.json
    msg = data.get("message", "")
    print(f"[RECU] : {msg}")
    
    if msg:
        # Réponse via tinydolphin
        subprocess.run(["python3", "voix.py", f"Confirmation. {msg}"])
        return jsonify({"status": "success", "reply": "Bien reçu"}), 200
    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    # Écoute sur 0.0.0.0 pour être accessible par l'IP Android
    app.run(host='0.0.0.0', port=5000)
