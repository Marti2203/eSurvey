from threading import Thread
from subprocess import call
from playsound import *
dev_null = open("/dev/null","w")
class Speaker(Thread):
    def __init__(self,file_path):
        super().__init__()
        self.file_path = file_path
    
    def run(self):
        playsound(self.file_path)
        #call(["espeak", "", stdout = dev_null, stderr=dev_null)
        pass
