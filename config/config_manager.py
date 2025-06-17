
import json
import os
from utils.logger import log

class ConfigManager:
    def __init__(self, config_path="profiles/profiles.json"):
        self.config_path = config_path
        self.config = {
            "mappings": {},
            "failsafe": [1500]*10
        }
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_path):
            log("Nessun file di configurazione trovato. Creazione nuovo file...")
            self.save_config()
        else:
            try:
                with open(self.config_path, "r") as f:
                    self.config = json.load(f)
                log("Configurazione caricata con successo.")
            except Exception as e:
                log(f"Errore caricamento config: {e}")
                self.save_config()

    def save_config(self):
        try:
            with open(self.config_path, "w") as f:
                json.dump(self.config, f, indent=4)
            log("Configurazione salvata.")
        except Exception as e:
            log(f"Errore salvataggio config: {e}")

    def get_mapping(self, input_code):
        return self.config["mappings"].get(input_code, None)

    def set_mapping(self, input_code, channel):
        self.config["mappings"][input_code] = channel
        self.save_config()

    def get_failsafe(self):
        return self.config["failsafe"]

    def set_failsafe(self, channel, value):
        self.config["failsafe"][channel] = value
        self.save_config()
