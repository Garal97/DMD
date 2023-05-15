import serial
import time
import os
import pafy
#arduino = serial.Serial ("COM5", 9600)
time.sleep (2)
webm_files = ""
filename = ""
x = 1
def audio_download ():
    audio = pafy.new (url)
    bestaudio = audio.getbestaudio()
    bestaudio.download()

def get_file_name ():
    webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
    filename = webm_files [0]
    print (filename)

def open_file ():
    os.startfile (filename)

def delete_file ():
    os.remove (filename)
    print ("File removed")

def close_vlc ():
    os.system ("taskkill /im vlc.exe")

webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
if len (webm_files) ==1:
    os.remove (filename)

while True:
    print ("X: ", x)
    value = input ("Introduzca un valor: ")
    if value == "0":
        print ("Got Here")
        url = "https://www.youtube.com/watch?v=wLlovxa3VJ0"
        if x == 0:
            delete_file()
        if x == 1:
            x = 0
        #close_vlc ()
        audio_download ()
        get_file_name()
        #open_file ()
    if value == "1":
        url = "https://www.youtube.com/watch?v=WVkD4lgXTEU"
        if x == 0:
            os.remove (filename)
        if x == 1:
            x = 0
        #close_vlc ()
        audio_download ()
        get_file_name()
        #open_file ()
    
        