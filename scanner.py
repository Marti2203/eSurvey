import serial
import os
from threading import Thread
class BarcodeScanner(Thread):
    def __init__(self,win):
        super().__init__()
        super().setDaemon(True)
        self.scanner_path = '/dev/ttyUSB0'
        self.patient_id = ''
        self.win = win

    def run(self):
        while not os.path.exists(self.scanner_path):
            pass
        self.ser = serial.Serial(self.scanner_path ,9600, 8, 'N', 1,timeout=0.1)
        while True:
            output = self.ser.readline()[:-2].decode("utf-8")
            if output != "" and self.patient_id == "":
                self.patient_id = output
                self.win.event_generate("<<start_logic>>")
    
    def get_patient_id(self):
        x = self.patient_id
        self.patient_id = ''
        return x
