
import threading
import hid
import time
from utils.logger import log

class HIDReader(threading.Thread):
    def __init__(self, config_manager, serial_tx):
        super().__init__()
        self.config = config_manager
        self.serial_tx = serial_tx
        self.running = True
        self.device_list = []
        self.detect_devices()

    def detect_devices(self):
        self.device_list = hid.enumerate()
        log(f"Dispositivi HID trovati: {len(self.device_list)}")
        for idx, device in enumerate(self.device_list):
            log(f"{idx+1}: {device['product_string']} (VID:{device['vendor_id']} PID:{device['product_id']})")

    def run(self):
        while self.running:
            for device in self.device_list:
                try:
                    h = hid.device()
                    h.open_path(device['path'])
                    data = h.read(64, timeout_ms=50)
                    if data:
                        self.process_data(data)
                    h.close()
                except Exception as e:
                    log(f"Errore HID su {device['product_string']}: {e}")
            time.sleep(0.01)

    def process_data(self, data):
        channel_values = [1500] * 10
        if len(data) > 0:
            channel_values[0] = 1500 + int((data[0]-128)*4)
        self.serial_tx.send(channel_values)

    def stop(self):
        self.running = False
