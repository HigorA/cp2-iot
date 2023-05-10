from time import sleep

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
            texto = recon.recognize_google(audio, language='pt-BR')
            print(texto)
        return texto

    def falar(self, texto):
        mp3_fp = BytesIO()
        voz = gTTS(texto, lang='pt')
        voz.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        print('Falando...')
        mixer.init()
        mixer.music.load(mp3_fp)
        mixer.music.play()

        while mixer.music.get_busy():
            pass  # Aguarda até que a reprodução termine

        mixer.music.stop()
        mixer.quit()

    def previsao_tempo(self):
        pass

    def falar_hora(self):
        pass

    def ler_emails(self):
        pass

    def pesquisar(self):
        pass

    def reproduzir_audio(self):
        pass

    def ver_imagem(self):
        pass

    def cotacao(self):
        pass

    def adicionar_na_agenda(self):
        pass

    def ler_agenda(self):
        pass

    def adicionar_lembrete(self):
        pass

    def visualizar_lembrete(self):
        pass
