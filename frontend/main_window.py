
from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, config_manager, serial_tx):
        super().__init__()
        self.setWindowTitle("Formula RPV Control System 4.0")
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet("background-color: #111;")
        
        self.config = config_manager
        self.serial_tx = serial_tx

        self.title = QtWidgets.QLabel("FORMULA RPV CONTROL SYSTEM", self)
        self.title.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
        self.title.move(50, 30)
        
        self.sliders = []
        self.slider_labels = []
        for i in range(10):
            label = QtWidgets.QLabel(f"CH{i+1}", self)
            label.setStyleSheet("color: white; font-weight: bold;")
            label.setGeometry(50 + i*115, 100, 100, 30)
            self.slider_labels.append(label)
            
            slider = QtWidgets.QSlider(QtCore.Qt.Vertical, self)
            slider.setGeometry(50 + i*115, 150, 80, 400)
            slider.setMinimum(1000)
            slider.setMaximum(2000)
            slider.setValue(1500)
            slider.setStyleSheet("background-color: #222;")
            self.sliders.append(slider)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_serial)
        self.timer.start(50)

    def update_serial(self):
        values = [slider.value() for slider in self.sliders]
        self.serial_tx.send(values)
