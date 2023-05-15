import pafy
import vlc
url = "https://www.youtube.com/watch?v=iq21HNTMrjk"
video = pafy.new (url)
bestaudio = video.getbestaudio()
bestaudio.download()
instance = vlc.Instance()
#player = instance.media_player_new()
#media = instance.media_new (bestaudio)
#media.get_mrl ()
#player.set_media (media)
#player.play()
p = vlc.MediaPlayer ("POESÍA PROCEDIMENTAL - chusommontero 💧.webm")
p.play