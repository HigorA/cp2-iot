from gtts import gTTS
from pygame import mixer
from io import BytesIO
import speech_recognition as sr


class SextaFeira:

    def __init__(self):
        pass

    def ouvir(self):
        recon = sr.Recognizer()
        with sr.Microphone() as source:
            recon.adjust_for_ambient_noise(source, duration=3)
            print('Fale algo...')
            audio = recon.listen(source)
            print('Reconhecendo...')
        print(audio)

    def falar(self, texto):
        mp3_fp = BytesIO()
        voz = gTTS(texto, lang='pt')
        voz.write_to_fp(mp3_fp)
        print('Falando...')
        mixer.init()
        mixer.music.load(mp3_fp)

    def previsao_tempo(self):
        pass

    def hora(self):
        pass

    def ler_emails(self):
        pass

    def pesquisa(self):
        pass

    def tocar_musica(self):
        pass

    def ver_imagem(self):
        pass
