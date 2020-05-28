from gtts import gTTS
import pygame, requests, os

def Speak(text, language, volume):
    tts = gTTS(text=text, lang=language)
    
    url = tts.get_urls()
    r = requests.get(url[0])
    
    if os.path.exists("temp.mp3"):
        os.remove("temp.mp3")
    
    open("temp.mp3", "wb").write(r.content)

    pygame.mixer.init(48000, -16, 1, 1024)
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)