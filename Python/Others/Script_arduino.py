import serial       
import time
import os
import pafy
import pygetwindow as gw
import keyboard as kb
arduino = serial.Serial ("COM5", 9600)  #empiezo la comunicacion con el arduino
time.sleep (2)  #le doy tiempo a que establezca la conexion
filename = ""   #variable global

#*********************************************************************************
def audio_download ():
    audio = pafy.new (url)
    bestaudio = audio.getbestaudio()
    bestaudio.download()        #descarga el audio de una url

def get_file_name ():
    webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
    filename = webm_files [0]
    print (filename)        #comprueba el nombre de un archivo con una extension .webm

def open_file ():
    os.startfile (filename)
    print ("opened!")       #abre un archivo

def delete_file ():
    webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
    filename = webm_files [0]
    os.remove (filename)
    print ("File removed")      #borra un archivo

def close_vlc ():
    os.system ("taskkill /im vlc.exe")  #mata el proceso del vlc

#**********************************************************************************

#remove all .webm files from the working folder

os.system ("taskkill /im vlc.exe") #me aseguro de que el vlc este cerrado

webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
if len (webm_files) !=0:
    for i in range (0, len(webm_files)):
        os.remove (webm_files[i])       #borro los posibles archivos que haya en el directorio

print ("finished removing files")
x = 0
while True:     #bucle para la lectura del arduino
    rawString = arduino.readline()  #leo el puerto serie del arduino
    print(rawString.decode ('ascii'))
    print("************") 
    if rawString == b'Q\r\n':   #si pulso la Q en el teclado
        print ("Got Here")
        url = "https://www.youtube.com/watch?v=wLlovxa3VJ0" 
        os.system ("taskkill /im vlc.exe")
        if x == 1:
            webm_files = [f for f in os.listdir('.') if f.endswith('.webm')] #si habia algo abierto lo cierro
            filename = webm_files [0]
            os.remove (filename)
        if x == 0:
            x = 1
        audio_download ()
        time.sleep (2)
        webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
        filename = webm_files [0]
        open_file ()    #descargo el archivo y lo abro en vlc
    if rawString == b'W\r\n':
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
    if rawString == b'E\r\n':
        webm_files = [f for f in os.listdir('.') if f.endswith('.webm')]
        filename = webm_files [0]       #consigo el nombre de la ventana (igual que el archivo descargado)
        vlc_window = gw.getWindowsWithTitle (filename) [0]
        vlc_window.activate()   #activo la ventana
        kb.press_and_release ("space")  #play/pause
        kb.press ("alt")
        time.sleep (0.2)
        kb.press_and_release ("tab")
        time.sleep (0.2)
        kb.release ("alt")      #alt+tab para dejar al usuario en la ventana que estaba usando