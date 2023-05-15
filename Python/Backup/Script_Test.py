import serial
import time
import os
import pafy
#arduino = serial.Serial ("COM5", 9600)
time.sleep (2)
filename = ""

#*********************************************************************************
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
    print ("opened!")

def delete_file ():
    webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
    filename = webm_files [0]
    os.remove (filename)
    print ("File removed")

def close_vlc ():
    os.system ("taskkill /im vlc.exe")

#**********************************************************************************

#remove all .webm files from the working folder

os.system ("taskkill /im vlc.exe")

webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
if len (webm_files) !=0:
    for i in range (0, len(webm_files)):
        os.remove (webm_files[i])

print ("finished removing files")
x = 0
while True:
    print ("X: ", x)
    value = input ("Introduzca un valor: ")
    if value == "0":
        print ("Got Here")
        url = "https://www.youtube.com/watch?v=wLlovxa3VJ0"
        os.system ("taskkill /im vlc.exe")
        if x == 1:
            webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
            filename = webm_files [0]
            os.remove (filename)
        if x == 0:
            x = 1
        audio_download ()
        time.sleep (2)
        webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
        filename = webm_files [0]
        open_file ()
    if value == "1":
        url = "https://www.youtube.com/watch?v=WVkD4lgXTEU"
        os.system ("taskkill /im vlc.exe")
        if x == 1:
            webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
            filename = webm_files [0]
            os.remove (filename)
        if x == 0:
            x = 1
        audio_download ()
        time.sleep (2)
        webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
        filename = webm_files [0]
        open_file ()

    


'''def audio_download ():
    audio = pafy.new (url)
    bestaudio = audio.getbestaudio()
    bestaudio.download()

def get_file_name ():
    webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
    filename = webm_files [0]
    print (filename)

def open_file ():
    os.startfile (filename)
    print ("opened!")

def delete_file ():
    webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
    filename = webm_files [0]
    os.remove (filename)
    print ("File removed")

def close_vlc ():
    os.system ("taskkill /im vlc.exe")##'''