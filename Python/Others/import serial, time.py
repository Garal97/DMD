import serial
import time
import webbrowser
arduino = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)
tavern = "Q"
while True:
    rawString = arduino.readline()
    print(rawString.decode ('ascii'))
    print("************") 
    if rawString == b'Q\r\n':
        webbrowser.open('https://open.spotify.com/playlist/68R6Mcd9YS57A2mXN98KHZ')
        print ("Opened!")
