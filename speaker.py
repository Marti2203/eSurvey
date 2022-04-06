from threading import Thread
from subprocess import call
from playsound import *
import os
class Speaker(Thread):
    def __init__(self,file_path):
        super().__init__()
        self.file_path = file_path
    
    def run(self):
        if os.path.exists(self.file_path):
            playsound(self.file_path)
        #call(["espeak", "", stdout = dev_null, stderr=dev_null)
        pass
