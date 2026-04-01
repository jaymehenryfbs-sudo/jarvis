#!/bin/bash
echo "🚀 J.A.R.V.I.S. : INITIALISATION..."
sudo fuser -k 5000/tcp > /dev/null 2>&1
sleep 1
nohup python3 ~/jarvis/cerveau.py > ~/jarvis/cerveau.log 2>&1 &
echo "[✅] Cerveau en ligne sur le port 5000."
