import os 
import pafy
import time
url = "https://www.youtube.com/watch?v=iq21HNTMrjk"
video = pafy.new (url)
bestaudio = video.getbestaudio()
bestaudio.download()                    #instancia para descargar el audio
txt_files = [f for f in os.listdir('.') if f.endswith('.webm')]
#if len(txt_files) != 1:
#    raise ValueError('should be only one txt file in the current directory')
filename = txt_files [0]
os.startfile (filename)
time.sleep (5)
os.system("taskkill /im vlc.exe")
os.remove (filename)
url2 = "https://www.youtube.com/watch?v=hWPPD5ww0eA&t"
video = pafy.new (url2)
bestaudio = video.getbestaudio()
bestaudio.download()
txt_files = [f for f in os.listdir('.') if f.endswith('.webm')]
if len(txt_files) != 1:
    raise ValueError('should be only one txt file in the current directory')
filename = txt_files [0]
os.startfile (filename)
