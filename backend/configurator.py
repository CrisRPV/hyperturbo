import json
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

CONFIG_FILE = 'channels.json'

def load_config():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"channels": {}}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

@app.route('/get-config', methods=['GET'])
def get_config():
    config = load_config()
    return jsonify(config)

@app.route('/set-config', methods=['POST'])
def set_config():
    config = request.json
    save_config(config)
    return jsonify({"status": "saved"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
