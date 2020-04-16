from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle
from tkinter import messagebox
import os
from crontab import CronTab

def info():
    messagebox.showinfo('Info', '(c) Brnjak Dominik\n'
                                'Willkomen im aWATTar User Interface!\n'
                                '- Im Laufzeiten Dropdown-Menü können Sie die Stunden anpassen.\n'
                                '\n'
                                'ACHTUNG!\n'
                                'Änderungen VOR 14:00 werden für den selben Tag übernommen.\n'
                                'Änderungen NACH 14:00 werden für den folgenden Tag übernommen.\n'
                                '\n'
                                '- De bzw. Aktivieren und Quit-Button sind selbsterklärend.\n'
                                '- Statistik-Button generiert aus den Daten der Datenbank ein Diagramm über Preisentwickling und Verbraucherzeiten.\n'
                                '\n'
                                '- Have Fun Using!\n')
    
def plot():
    import subprocess
    subprocess.call("/home/pi/Python/UI/sqlplot.py")

def on():
    msg = messagebox.showinfo('Info', 'aWATTar wird aktiviert')
    print(radioValue.get())
    comboExample.config(state=NORMAL)
    comboExample1.config(state=NORMAL)
    comboExample2.config(state=NORMAL)
    comboExample3.config(state=NORMAL)
    import subprocess
    subprocess.call("/home/pi/Python/UI/ALLOFF.sh")
    print ("Erfolgreich")
 
def off():
    msg = messagebox.showinfo('Info', 'aWATTar wird deaktiviert')
    print(radioValue.get())
    comboExample.config(state=DISABLED)
    comboExample1.config(state=DISABLED)
    comboExample2.config(state=DISABLED)
    comboExample3.config(state=DISABLED)
    from crontab import CronTab
    cron = CronTab(user='pi')
    cron.remove_all(comment='m')
    cron.remove_all(comment='m2')
    cron.remove_all(comment='m3')
    cron.remove_all(comment='m4')
    cron.remove_all(comment='last1')
    cron.remove_all(comment='last1e')
    cron.remove_all(comment='last2')
    cron.remove_all(comment='last2e')
    cron.remove_all(comment='last3')
    cron.remove_all(comment='last3e')
    cron.remove_all(comment='last4')
    cron.remove_all(comment='last4e')
    cron.write() 
    import subprocess
    subprocess.call("/home/pi/Python/UI/ALLON.sh")
    print ("Erfolgreich")

def callbackFunc(event):
    msg=messagebox.askokcancel('Info für Last 1', 'Neue Laufzeit von '+ comboExample.get() +' Stunden speichern ?')
    if msg == True:
       print("Last 1 Neue Laufzeit:")
       print(comboExample.get()+" Stunden")
       messagebox.showinfo('Info', 'Erfolgreich gespeichert!')
       if int (comboExample.get()) == 1:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/1.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()
       if int (comboExample.get()) == 2:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/2.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()        
       if int (comboExample.get()) == 3:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/3.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()         
       if int (comboExample.get()) == 4:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/4.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()
       if int (comboExample.get()) == 5:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/5.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()
       if int (comboExample.get()) == 6:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/6.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()   
       if int (comboExample.get()) == 7:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/7.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()               
       if int (comboExample.get()) == 8:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/8.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()               
       if int (comboExample.get()) == 9:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/9.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()               
       if int (comboExample.get()) == 10:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/10.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()               
       if int (comboExample.get()) == 11:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/11.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()               
       if int (comboExample.get()) == 12:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/12.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()               
       if int (comboExample.get()) == 13:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/13.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()
       if int (comboExample.get()) == 14:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/14.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()
       if int (comboExample.get()) == 15:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/15.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()
       if int (comboExample.get()) == 16:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/16.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()   
       if int (comboExample.get()) == 17:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/17.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()
       if int (comboExample.get()) == 18:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/18.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()
       if int (comboExample.get()) == 19:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/19.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()               
       if int (comboExample.get()) == 20:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m')
            job = cron.new(command='/home/pi/Python/Last1/20.py', comment='m')
            job.hour.on(14)
            job.minute.on(11)
            cron.write()               
            
    if msg == False:
        messagebox.showinfo('Info', 'Nichts gespeichert!')
     
def callbackFunc1(event):
    msg=messagebox.askokcancel('Info für Last 2', 'Neue Laufzeit von '+ comboExample1.get() +' Stunden speichern ?')
    if msg == True:
       print("Last 2 Neue Laufzeit:")
       print(comboExample1.get()+" Stunden")
       messagebox.showinfo('Info', 'Erfolgreich gespeichert!')
       if int (comboExample1.get()) == 1:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/1.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()
       if int (comboExample1.get()) == 2:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/2.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()        
       if int (comboExample1.get()) == 3:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/3.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()         
       if int (comboExample1.get()) == 4:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/4.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()
       if int (comboExample1.get()) == 5:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/5.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()
       if int (comboExample1.get()) == 6:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/6.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()   
       if int (comboExample1.get()) == 7:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/7.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()               
       if int (comboExample1.get()) == 8:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/8.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()               
       if int (comboExample1.get()) == 9:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/9.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()               
       if int (comboExample1.get()) == 10:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/10.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()               
       if int (comboExample1.get()) == 11:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/11.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()               
       if int (comboExample1.get()) == 12:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/12.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()               
       if int (comboExample1.get()) == 13:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/13.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()
       if int (comboExample1.get()) == 14:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/14.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()
       if int (comboExample1.get()) == 15:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/15.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()
       if int (comboExample1.get()) == 16:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/16.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()   
       if int (comboExample1.get()) == 17:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/17.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()
       if int (comboExample1.get()) == 18:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/18.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()
       if int (comboExample1.get()) == 19:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/19.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()               
       if int (comboExample1.get()) == 20:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m2')
            job = cron.new(command='/home/pi/Python/Last2/20.py', comment='m2')
            job.hour.on(14)
            job.minute.on(12)
            cron.write()              
       
    if msg == False:
        messagebox.showinfo('Info', 'Nichts gespeichert!')
        
def callbackFunc2(event):
    msg=messagebox.askokcancel('Info für Last 3', 'Neue Laufzeit von '+ comboExample2.get() +' Stunden speichern ?')
    if msg == True:
       print("Last 3 Neue Laufzeit:")
       print(comboExample2.get()+" Stunden")
       messagebox.showinfo('Info', 'Erfolgreich gespeichert!')
       if int (comboExample2.get()) == 1:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/1.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()
       if int (comboExample2.get()) == 2:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/2.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()        
       if int (comboExample2.get()) == 3:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/3.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()         
       if int (comboExample2.get()) == 4:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/4.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()
       if int (comboExample2.get()) == 5:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/5.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()
       if int (comboExample2.get()) == 6:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/6.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()   
       if int (comboExample2.get()) == 7:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/7.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()               
       if int (comboExample2.get()) == 8:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/8.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()               
       if int (comboExample2.get()) == 9:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/9.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()               
       if int (comboExample2.get()) == 10:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/10.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()               
       if int (comboExample2.get()) == 11:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/11.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()               
       if int (comboExample2.get()) == 12:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/12.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()               
       if int (comboExample2.get()) == 13:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/13.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()
       if int (comboExample2.get()) == 14:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/14.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()
       if int (comboExample2.get()) == 15:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/15.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()
       if int (comboExample2.get()) == 16:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/16.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()   
       if int (comboExample2.get()) == 17:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/17.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()
       if int (comboExample2.get()) == 18:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/18.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()
       if int (comboExample2.get()) == 19:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/19.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()               
       if int (comboExample2.get()) == 20:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m3')
            job = cron.new(command='/home/pi/Python/Last3/20.py', comment='m3')
            job.hour.on(14)
            job.minute.on(13)
            cron.write()              
       
    if msg == False:
        messagebox.showinfo('Info', 'Nichts gespeichert!')
     
def callbackFunc3(event):
    msg=messagebox.askokcancel('Info für Last 4', 'Neue Laufzeit von '+ comboExample3.get() +' Stunden speichern ?')
    if msg == True:
       print("Last 4 Neue Laufzeit:")
       print(comboExample3.get()+" Stunden")
       messagebox.showinfo('Info', 'Erfolgreich gespeichert!')
       if int (comboExample3.get()) == 1:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/1.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()
       if int (comboExample3.get()) == 2:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/2.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()        
       if int (comboExample3.get()) == 3:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/3.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()         
       if int (comboExample3.get()) == 4:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/4.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()
       if int (comboExample3.get()) == 5:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/5.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()
       if int (comboExample3.get()) == 6:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/6.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()   
       if int (comboExample3.get()) == 7:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/7.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()               
       if int (comboExample3.get()) == 8:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/8.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()               
       if int (comboExample3.get()) == 9:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/9.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()               
       if int (comboExample3.get()) == 10:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/10.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()               
       if int (comboExample3.get()) == 11:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/11.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()               
       if int (comboExample3.get()) == 12:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/12.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()               
       if int (comboExample3.get()) == 13:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/13.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()
       if int (comboExample3.get()) == 14:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/14.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()
       if int (comboExample3.get()) == 15:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/15.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()
       if int (comboExample3.get()) == 16:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/16.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()   
       if int (comboExample3.get()) == 17:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/17.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()
       if int (comboExample3.get()) == 18:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/18.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()
       if int (comboExample3.get()) == 19:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/19.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()               
       if int (comboExample3.get()) == 20:
            from crontab import CronTab
            cron = CronTab(user='pi')
            cron.remove_all(comment='m4')
            job = cron.new(command='/home/pi/Python/Last4/20.py', comment='m4')
            job.hour.on(14)
            job.minute.on(14)
            cron.write()                     
       
    if msg == False:
        messagebox.showinfo('Info', 'Nichts gespeichert!')
 
root = tk.Tk()
img = Image("photo", file="icon (1).gif")
root.tk.call('wm','iconphoto',root._w,img)
root.geometry('200x100')
root.title("Raspberry aWATTar User Interface")
root.config(background = "#F2F2F2")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# Setting Theme
style = ThemedStyle(root)
style.set_theme("ubuntu")

#Bild anlegen und positionieren
image1 = PhotoImage(file="bbb.png")
panel1 = Label(root, image = image1, background="#F2F2F2")
panel1.config(height=900, width=1920)
panel1.place(x=-3, y=25, relheight=1, relwidth=1)

style.configure('TButton', width = 15, borderwidth=1, background = "#F2F2F2", font=('Verdana', 16))
Themed_Btn = ttk.Button(root,text='EXIT', command=quit)
Themed_Btn.place(x=1645, y=0)

Themed_Btn1 = ttk.Button(root,text='INFO', command=info)
Themed_Btn1.place(x=1645, y=43)

Themed_Btn1 = ttk.Button(root,text='STATISTIK', command=plot)
Themed_Btn1.place(x=1645, y=86)


import tkinter.ttk as ttk

myColor = '#F2F2F2'                         
s = ttk.Style()                     
s.configure('Wild.TRadiobutton',    
        background=myColor,         
        font = ('Verdana' , 16))    


#Radiobuttons On/Off
radioValue = tk.StringVar()
radioValue.set("Aktiviert") 

 
rdioOne = ttk.Radiobutton(root, text='Aktivieren', style = 'Wild.TRadiobutton',  
                             variable=radioValue, value="Aktiviert", command=on) 
rdioTwo = ttk.Radiobutton(root, text='Deaktivieren',  style = 'Wild.TRadiobutton',
                             variable=radioValue, value= "Deaktivert", state=DISABLED, command=off) 

rdioOne.grid(column=5, row=2, padx=8, pady=1)
rdioTwo.grid(column=6, row=2, padx=8, pady=1)

labelValue = ttk.Label(root, textvariable=radioValue, font=("Verdana", 16), background="")
labelValue.grid(column=5, row=1, columnspan=2)

# Hier kommen die Elemente hin
leftFrame = Frame(root, width=300, height = 500, background="#F2F2F2")
leftFrame.grid(row=0, column=0, rowspan=4, padx=10, pady=1)

# Hier kommen die Elemente hin
leftLabel1 = Label(leftFrame, text="  aWATTar User Interface", font=("Verdana", 16), background="#F2F2F2")
leftLabel1.grid(row=0, column=0, padx=1, pady=1)
leftLabel2 = Label(leftFrame, text="  Energy in Sync with Nature", font=("Verdana", 16), background="#F2F2F2")
leftLabel2.grid(row=1, column=0, padx=1, pady=5)

imageEx = PhotoImage(file = 'awattar.png')
Label(leftFrame, image=imageEx, background="#F2F2F2").grid(row=2, column=0, padx=0, pady=5)

#Uhr
from tkinter import font
import time
import datetime
#now = datetime.datetime.now()


def show_time():
    txt.set(time.strftime("%H:%M:%S"))
    root.after(1000, show_time)

root.after(1000, show_time)


def show_date():
    txt1.set(time.strftime("%d.%m.%Y"))
    root.after(1000, show_date)

root.after(1000, show_date)

def show1():
    from crontab import CronTab

    my_cron = CronTab(user='pi')
    for job in my_cron:
        if job.comment == 'last1':
           #print (str(job)[2:4])
           x = str(job)[2:5]
    for job1 in my_cron:
        if job1.comment == 'last1e':
           #print (str(job1)[2:4])
           y = str(job1)[2:5]
       
    strObj = "      Aktuell: \nStart um " +x+ " Uhr \nEnde um " +y+ " Uhr"
    #print (strObj)
    txt2.set(strObj)
    root.after(1000, show1)

root.after(1000, show1)

def show2():
    from crontab import CronTab

    my_cron = CronTab(user='pi')
    for job in my_cron:
        if job.comment == 'last2':
           #print (str(job)[2:4])
           x1 = str(job)[2:5]
    for job1 in my_cron:
        if job1.comment == 'last2e':
           #print (str(job1)[2:4])
           y1 = str(job1)[2:5]
       
    strObj1 = "      Aktuell: \nStart um " +x1+ " Uhr \nEnde um " +y1+ " Uhr"
    #print (strObj)
    txt3.set(strObj1)
    root.after(1000, show2)

root.after(1000, show2)

def show3():
    from crontab import CronTab

    my_cron = CronTab(user='pi')
    for job in my_cron:
        if job.comment == 'last3':
           #print (str(job)[2:4])
           x2 = str(job)[2:5]
    for job1 in my_cron:
        if job1.comment == 'last3e':
           #print (str(job1)[2:4])
           y2 = str(job1)[2:5]
       
    strObj2 = "      Aktuell: \nStart um " +x2+ " Uhr \nEnde um " +y2+ " Uhr"
    #print (strObj)
    txt4.set(strObj2)
    root.after(1000, show3)

root.after(1000, show3)


def show4():
    from crontab import CronTab

    my_cron = CronTab(user='pi')
    for job in my_cron:
        if job.comment == 'last4':
           #print (str(job)[2:4])
           x3 = str(job)[2:5]
    for job1 in my_cron:
        if job1.comment == 'last4e':
           #print (str(job1)[2:4])
           y3 = str(job1)[2:5]
       
    strObj3 = "      Aktuell: \nStart um " +x3+ " Uhr \nEnde um " +y3+ " Uhr"
    #print (strObj)
    txt5.set(strObj3)
    root.after(1000, show4)

root.after(1000, show4)


fnt = font.Font(family='Verdana', size=90, weight='bold')
txt = StringVar()
txt.set(time.strftime("%H:%M:%S"))
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="#a9d400", background="#F2F2F2")
lbl.place(x=1200, y=210)

fnt = font.Font(family='Verdana', size=50, weight='bold')
txt1 = StringVar()
txt1.set(time.strftime("%d.%m.%Y"))
lb2 = ttk.Label(root, textvariable=txt1, font=fnt, foreground="#a9d400", background="#F2F2F2")
lb2.place(x=1210, y=350)

#Last 1 Info
fnt = font.Font(family='Verdana', size=14)
txt2 = StringVar()

from crontab import CronTab

my_cron = CronTab(user='pi')
for job in my_cron:
    if job.comment == 'last1':
       #print (str(job)[2:4])
       x = str(job)[2:5]
for job1 in my_cron:
    if job1.comment == 'last1e':
       #print (str(job1)[2:4])
       y = str(job1)[2:5]
       
strObj = "      Aktuell: \nStart um " +x+ " Uhr \nEnde um " +y+ " Uhr"
#print (strObj)

txt2.set(strObj)
lbl = ttk.Label(root, textvariable=txt2, font=fnt, background="#F2F2F2")
lbl.place(x=375, y=130)

#Info Last2
fnt = font.Font(family='Verdana', size=14)
txt3 = StringVar()

my_cron = CronTab(user='pi')
for job in my_cron:
    if job.comment == 'last2':
       #print (str(job)[2:4])
       x1 = str(job)[2:5]
for job1 in my_cron:
    if job1.comment == 'last2e':
       #print (str(job1)[2:4])
       y1 = str(job1)[2:5]
       
strObj1 = "      Aktuell: \nStart um " +x1+ " Uhr \nEnde um " +y1+ " Uhr"
#print (strObj)

txt3.set(strObj1)
lbl = ttk.Label(root, textvariable=txt3, font=fnt, background="#F2F2F2")
lbl.place(x=615, y=130)

#Last 3
fnt = font.Font(family='Verdana', size=14)
txt4 = StringVar()

my_cron = CronTab(user='pi')
for job in my_cron:
    if job.comment == 'last3':
       #print (str(job)[2:4])
       x2 = str(job)[2:5]
for job1 in my_cron:
    if job1.comment == 'last3e':
       #print (str(job1)[2:4])
       y2 = str(job1)[2:5]
       
strObj2 = "      Aktuell: \nStart um " +x2+ " Uhr \nEnde um " +y2+ " Uhr"
#print (strObj)

txt4.set(strObj2)
lbl = ttk.Label(root, textvariable=txt4, font=fnt, background="#F2F2F2")
lbl.place(x=855, y=130)


#Info Last 4
fnt = font.Font(family='Verdana', size=14)
txt5 = StringVar()

my_cron = CronTab(user='pi')
for job in my_cron:
    if job.comment == 'last4':
       #print (str(job)[2:4])
       x3 = str(job)[2:5]
for job1 in my_cron:
    if job1.comment == 'last4e':
       #print (str(job1)[2:4])
       y3 = str(job1)[2:5]
       
strObj3 = "      Aktuell: \nStart um " +x3+ " Uhr \nEnde um " +y3+ " Uhr"
#print (strObj)

txt5.set(strObj3)
lbl = ttk.Label(root, textvariable=txt5, font=fnt, background="#F2F2F2")
lbl.place(x=1095, y=130)


#Optionen
labelTop = ttk.Label(root,
                    text = "OPTIONEN", font=("Verdana", 18))
labelTop.grid(column=5, row=0, columnspan=2, padx=30, pady=3)

#Last 1 Dropdown
labelTop = ttk.Label(root,
                    text = "LAST 1", font=("Verdana", 18))
labelTop.grid(column=1, row=0, padx=30, pady=0)

labelTop = ttk.Label(root,
                    text = "Laufzeit wählen ", font=("Verdana", 16))
labelTop.grid(column=1, row=1, padx=30, pady=0)

comboExample = ttk.Combobox(root,  
                            values=[
                                    "1", 
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7",
                                    "8",
                                    "9",
                                    "10",
                                    "11",
                                    "12",
                                    "13",
                                    "14",
                                    "15",
                                    "16",
                                    "17",
                                    "18",
                                    "19",
                                    "20"],width=11, font="Verdana 17",)

comboExample.grid(column=1, row=2, padx=30, pady=0)
comboExample.current(1)

comboExample.bind("<<ComboboxSelected>>", callbackFunc)

#Last 2 Dropdown

labelTop1 = ttk.Label(root,
                    text = "LAST 2", font=("Verdana", 18))
labelTop1.grid(column=2, row=0, padx=30, pady=0)

labelTop1 = ttk.Label(root,
                    text = "Laufzeit wählen ", font=("Verdana", 16))
labelTop1.grid(column=2, row=1, padx=30, pady=0)

comboExample1 = ttk.Combobox(root, 
                            values=[
                                    "1", 
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7",
                                    "8",
                                    "9",
                                    "10",
                                    "11",
                                    "12",
                                    "13",
                                    "14",
                                    "15",
                                    "16",
                                    "17",
                                    "18",
                                    "19",
                                    "20"],width=11, font="Verdana 17")

comboExample1.grid(column=2, row=2, padx=30, pady=0)
comboExample1.current(1)

comboExample1.bind("<<ComboboxSelected>>", callbackFunc1)

#Last 3 Dropdown

labelTop2 = ttk.Label(root,
                    text = "LAST 3", font=("Verdana", 18))
labelTop2.grid(column=3, row=0, padx=30, pady=0)

labelTop2 = ttk.Label(root,
                    text = "Laufzeit wählen ", font=("Verdana", 16))
labelTop2.grid(column=3, row=1, padx=30, pady=0)

comboExample2 = ttk.Combobox(root, 
                            values=[
                                    "1", 
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7",
                                    "8",
                                    "9",
                                    "10",
                                    "11",
                                    "12",
                                    "13",
                                    "14",
                                    "15",
                                    "16",
                                    "17",
                                    "18",
                                    "19",
                                    "20"],width=11, font="Verdana 17")

comboExample2.grid(column=3, row=2, padx=30, pady=0)
comboExample2.current(1)

comboExample2.bind("<<ComboboxSelected>>", callbackFunc2)

#Last 4 Dropdown
labelTop3 = ttk.Label(root,
                    text = "LAST 4", font=("Verdana", 18))
labelTop3.grid(column=4, row=0, padx=30, pady=0)

labelTop3 = ttk.Label(root,
                    text = "Laufzeit wählen ", font=("Verdana", 16))
labelTop3.grid(column=4, row=1, padx=30, pady=0)

comboExample3 = ttk.Combobox(root, 
                            values=[
                                    "1", 
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7",
                                    "8",
                                    "9",
                                    "10",
                                    "11",
                                    "12",
                                    "13",
                                    "14",
                                    "15",
                                    "16",
                                    "17",
                                    "18",
                                    "19",
                                    "20"],width=11, font="Verdana 17")

comboExample3.grid(column=4, row=2, padx=30, pady=0)
comboExample3.current(1)

comboExample3.bind("<<ComboboxSelected>>", callbackFunc3)

root.option_add('*TCombobox*Listbox.font', "Verdana 17")
root.mainloop()

