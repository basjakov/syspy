import platform
import os
import glob

class Computer:
        def CpuInfo(self):
            uname = platform.uname()
            info =  {
                   'uname':uname.system,
                   'NodeName':uname.node,
                   'Release':uname.release,
                   'Version':uname.version,
                   'Machine':uname.machine,
                   'Processor':uname.processor
                   }
            return info
        def TempCleaner(self):
            files = glob.glob('C:/Users/'+ os.getlogin() + '/AppData/Local/Temp/*')
            for f in files:
                os.remove(f)    
