import serial
import time
import os
import pafy
import pygetwindow as gw
import keyboard as kb
import serial.tools.list_ports
import config
import random
import pygetwindow as gw
from config import keyData, keyMode

COM_PORTS = []

global port
port = ''
global arduino

keys = [
    'key0',
    'key1',
    'key2',
    'key3',
    'key4',
    'key5',
    'key6',
    'key7',
    'key8'  
]

def checkCOM():
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid  in sorted (ports):
            COM_PORTS.append ("{}: {}".format(port, desc,))
            hwid = hwid #Compruebo todos los puertos como y los guardo en el array para usarlo en app.py

def checkMode ():
    if config.keyMode == '0':
        playMusic()
        print ('Lets play some music!')
    if config.keyMode == '1':
        print ('BEHOLD THE D20')
        rollDice()
    if config.keyMode == '2':
        openResource()
    else:
        print ('No match found')    #compruebo que modo tiene asignado la tecla con ayuda del archivo de configuraciones

def playMusic():
    os.system ('taskkill /im vlc.exe') #NECESARIO DESCARGAR LA MUSICA PRIMERO!!
    os.startfile (config.keyFile) #abro el archivo del path segun el archivo de configuracones
    config.latest_file (config.keyFile)

def rollDice():
    diceType = int (config.keyData [1:]) #la variable diceType es el string data sin el primer caracter convertido en int; str = 'd20' to int = 20 
    roll = random.randint (1, diceType) #tiro el dado
    print (roll)
    print (diceType) 
    dice =  str ('D') + str (diceType)
    print (dice)
    arduino.write(bytes(dice, 'utf-8'))
    time.sleep (0.1)
    arduino.write(bytes('r'+str(roll), 'utf-8')) #le doy formato a los strings y los envio por el puerto serie al arduino

def openResource ():

    os.startfile (config.keyData) #abre el recurso segun el path del archivo de configuraciones

def play_pause ():
    vlc_window = gw.getWindowsWithTitle (config.audioFile) [0] #agarra el handle de la ventana segun el nombre del archivo de configuracion
    vlc_window.activate()   #activo la ventana
    kb.press_and_release ("space") #shortcut para play/pause
    kb.press_and_release ('windows + down arrow') #shortcut para minimizar la ventana


def volumeUp ():
    vlc_window = gw.getWindowsWithTitle (config.audioFile) [0]
    vlc_window.activate()   #activo la ventana
    kb.press_and_release ('ctrl + up arrow') #shorcut para subir el volumen
    time.sleep (0.1)
    kb.press_and_release ('windows + down arrow')

def volumeDown ():
    vlc_window = gw.getWindowsWithTitle (config.audioFile) [0]
    vlc_window.activate()   #activo la ventana
    kb.press_and_release ('ctrl + down arrow') #shortcut para bajar el volumen
    time.sleep (0.1)
    kb.press_and_release ('windows + down arrow')



def initializeDMD ():


    webm_files = [f for f in os.listdir('.') if f.endswith('.webm')] #busco todos los archivos con extension ".webm" dentro del directorio
    if len (webm_files) !=0:
        for i in range (0, len(webm_files)):
            os.remove (webm_files[i])       #borro los posibles archivos que haya en el directorio  

    print ('Files removed')




def downloadMusic ():
    for c in range (0, 9): #reviso la configuracion de las teclas una por una
        config.read (keys [c])
        print ('Working on ' + keys[c]) 
        if  config.keyMode == '0': #si estan en modo musica descargo la cancion
            audio = pafy.new (config.keyData)
            bestaudio = audio.getbestaudio()
            bestaudio.download()        #descarga el audio de una url
            webm_files = [f for f in os.listdir('.') if f.endswith('.webm')] #busco todos los archivos .webm
            musicFile = webm_files [-1] #al ultimo archico de la lista le pongo un 0 delante para el orden alfabetico
            musicFile_old = musicFile
            musicFile = '0' + musicFile
            os.rename (musicFile_old, musicFile)
            config.updateName (keys[c], musicFile) #lo guardo en el archivo de configuracion
    print ('finished downloading')


            

def runDMD():
    global arduino
    arduino = serial.Serial (port, 115200) #inicializo la configuracion con arduino
    while True:

        rawString = arduino.readline()
        print (rawString)
        if rawString == b'Q\r\n':   #dependiendo del valor que lea, realizo una accion u otra con una key diferente
            print ('Pressed!')
            key = 'key0'
            config.read (key)
            checkMode()

        if rawString == b'W\r\n':
            print ('Pressed!')
            key = 'key1'
            config.read (key)
            checkMode()

        if rawString == b'E\r\n':
            print ('Pressed!')
            key = 'key2'
            config.read (key)
            checkMode()

        if rawString == b'A\r\n':
            print ('Pressed!')
            key = 'key3'
            config.read (key)
            checkMode()

        if rawString == b'S\r\n':
            print ('Pressed!')
            key = 'key4'
            config.read (key)
            checkMode()

        if rawString == b'D\r\n':
            print ('Pressed!')
            key = 'key5'
            config.read (key)
            checkMode()

        if rawString == b'Z\r\n':
            print ('Pressed!')
            key = 'key6'
            config.read (key)
            checkMode()

        if rawString == b'X\r\n':
            print ('Pressed!')
            key = 'key7'
            config.read (key)
            checkMode()

        if rawString == b'C\r\n':
            print ('Pressed!')
            key = 'key8'
            config.read (key)
            checkMode()   

        if rawString == b'Pressed!\r\n':
            play_pause()

        if rawString == b'1\r\n':
            volumeUp ()

        if rawString == b'2\r\n':
            volumeDown()