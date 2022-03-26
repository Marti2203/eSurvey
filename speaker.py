from threading import Thread
from subprocess import call
dev_null = open("/dev/null","w")
class Speaker(Thread):
    def __init__(self,file_path):
        super().__init__()
    
    def run(self):
        #call(["espeak", "", stdout = dev_null, stderr=dev_null)
        pass
