
import serial
import threading
from utils.logger import log

class SerialTransmitter:
    def __init__(self, port="COM3", baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.lock = threading.Lock()
        self.connect()

    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
            log(f"Serial connesso su {self.port} a {self.baudrate} bps")
        except serial.SerialException as e:
            log(f"Errore seriale: {e}")

    def send(self, channel_values):
        if not self.ser or not self.ser.is_open:
            log("Porta seriale non aperta")
            return
        try:
            packet = ",".join(str(val) for val in channel_values) + "\n"
            with self.lock:
                self.ser.write(packet.encode())
        except Exception as e:
            log(f"Errore invio seriale: {e}")

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            log("Serial chiuso")
