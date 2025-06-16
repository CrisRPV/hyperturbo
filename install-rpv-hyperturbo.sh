#!/bin/bash

echo "Formula RPV HyperTurbo Installer - Build 1.0.0"

# Aggiornamento pacchetti
sudo apt update && sudo apt upgrade -y

# Installazione dipendenze principali
sudo apt install -y python3 python3-pip python3-venv git unzip

# Creazione ambiente virtuale Python
python3 -m venv env
source env/bin/activate

# Installazione librerie Python richieste
pip install flask flask-cors pyserial inputs

echo "Installazione backend completata."

# Setup backend avvio automatico
(crontab -l 2>/dev/null; echo "@reboot cd $(pwd)/backend && ./start-backend.sh") | crontab -

echo "Installazione completata con successo!"
