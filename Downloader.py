from tkinter import messagebox
import subprocess  
import requests






class Downloader:
    def AdwCln(self):
        url = 'https://downloads.malwarebytes.com/file/adwcleaner'
        r = requests.get(url, allow_redirects=True)
        if open('soft/adwcleaner.exe', 'wb').write(r.content):
            messagebox.showinfo("SysPy Antivirus", "AdwCleaner downloaded successfully")

    def KasVrt(self):
        url = 'https://devbuilds.s.kaspersky-labs.com/devbuilds/KVRT/latest/full/KVRT.exe'
        r = requests.get(url, allow_redirects=True)
        if open('soft/KVRT.exe', 'wb').write(r.content):
            messagebox.showinfo("SysPy Antivirus", "Kaspersky virus removal tool downloaded successfully")
    def CureIt(self):
        url = 'https://free.drweb.com/download+cureit/gr/?lng=en'
        r = requests.get(url, allow_redirects=True)
        if open('soft/cureit.exe', 'wb').write(r.content):
            messagebox.showinfo("SysPy Antivirus", "DrWeb cure it downloaded successfully")  

           