from pygame import mixer


class TocarMusica:

    def __init__(self):
        pass

    def tocar_musica(self):
        mixer.init()
        mixer.music.load("musica1.mp3")
        mixer.music.play()

        while mixer.music.get_busy():
            pass

        mixer.music.stop()
        mixer.quit()

