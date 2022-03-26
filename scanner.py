import serial
from threading import Thread
class BarcodeScanner(Thread):
    def __init__(self,win):
        super().__init__()
        super().setDaemon(True)
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1,timeout=0.1)
        self.patient_id = ''

    def run(self):
        while True:
            output = self.ser.readline()[:-2].decode("utf-8")
            if output != "" and patient_id == "":
                self.patient_id = output
                self.win.event_generate("<<start_logic>>")
    
    def get_patient_id(self):
        x = self.patient_id
        self.patient_id = ''
        return x
