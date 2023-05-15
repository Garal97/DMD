import pafy
url_1 = "https://www.youtube.com/watch?v=iq21HNTMrjk"
url_2 = "https://www.youtube.com/watch?v=RMtJPqAExtw"
url_3 = "https://www.youtube.com/watch?v=uMyuSHewmks&t"
video = pafy.new (url_1)
bestaudio = video.getbestaudio()
bestaudio.download()                    
video = pafy.new (url_2)
bestaudio = video.getbestaudio()
bestaudio.download()                    
video = pafy.new (url_3)
bestaudio = video.getbestaudio()
bestaudio.download()                    