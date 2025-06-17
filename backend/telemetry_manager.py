
import time
from utils.logger import log

class TelemetryManager:
    def __init__(self):
        self.data_buffer = []
        self.max_buffer_size = 1000
        log("Modulo Telemetria inizializzato")

    def push_data(self, telemetry_data):
        timestamp = time.time()
        entry = {"time": timestamp, "data": telemetry_data}
        self.data_buffer.append(entry)
        
        if len(self.data_buffer) > self.max_buffer_size:
            self.data_buffer.pop(0)

    def get_latest(self):
        if self.data_buffer:
            return self.data_buffer[-1]
        return None

    def export_log(self, filepath):
        try:
            import json
            with open(filepath, "w") as f:
                json.dump(self.data_buffer, f, indent=4)
            log(f"Log telemetria esportato in {filepath}")
        except Exception as e:
            log(f"Errore export telemetria: {e}")
