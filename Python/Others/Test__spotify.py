import webbrowser, subprocess
URL = "https://open.spotify.com/playlist/68R6Mcd9YS57A2mXN98KHZ"
x = "7"
while True:
    y = input ("Introduce un número: ")
    if y == x:
        #webbrowser.open (URL)
        print ("Correcto!")
        subprocess.call (r'C:\Users\kinga\AppData\Roaming\Spotify\Spotify.exe')
    


        