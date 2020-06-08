import tkinter as tk
from Downloader import *
from computer import *

Download = Downloader()
Computer = Computer()
#downloads delegates
AdwCln = Download.AdwCln
KasVrt = Download.KasVrt
CureIt = Download.CureIt

CpuInfo = Computer.CpuInfo
comp = Computer.TempCleaner

Frm = tk.Tk()
Frm.geometry("750x600")
Frm.title("Syspy")


#ADW cleaner button
tk.Button(Frm,text="AdwCleaner",command=AdwCln).pack()
#Kaspersky virus removal tool
tk.Button(Frm,text="Kaspersky VRT",command=KasVrt).pack()
#DR web cureit
tk.Button(Frm,text="Dr Web CureIt",command=CureIt).pack()
#DR web cureit
tk.Button(Frm,text="Clear temp",command=comp).pack()
#DR web cureit
tk.Label(Frm, textvariable=CpuInfo).pack()



Frm.mainloop()

