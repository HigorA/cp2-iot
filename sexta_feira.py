from gtts import gTTS
from pygame import mixer
from io import BytesIO
import speech_recognition as sr

from funcionalidades.calculadora import Calculadora
from funcionalidades.agenda import Agenda
from funcionalidades.conversao_dolar import ConversaoDolar
from funcionalidades.cotacao import Cotacao
from funcionalidades.imc import IMC
from funcionalidades.previsao_tempo import PrevisaoTempo
from funcionalidades.tocar_musica import TocarMusica
from funcionalidades.ver_hora import VerHora
from funcionalidades.ver_imagem import VerImagem


class SextaFeira:

    def __init__(self):
        pass

    @staticmethod
    def ouvir():
        recon = sr.Recognizer()
        with sr.Microphone() as source:
            recon.adjust_for_ambient_noise(source, duration=5)
            print('Fale algo...')
            audio = recon.listen(source)
            print('Reconhecendo...')
            texto = recon.recognize_google(audio, language='pt-BR')
            print(texto)
        return texto

    @staticmethod
    def falar(texto):
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

    #  no menu
    def previsao_tempo(self, local):
        obj = PrevisaoTempo()
        retorno = obj.previsao(local)
        self.falar(retorno)

    def falar_hora(self):
        obj = VerHora()
        retorno = obj.hora_atual()
        self.falar(retorno)

    def calculadora(self, valor1, valor2):
        obj = Calculadora(valor1, valor2)
        self.falar('Qual das 4 operações básicas você deseja realizar?')
        operacao = self.ouvir()
        self.falar(obj.calcular(operacao))

    def imc(self):
        obj = IMC()
        self.falar('Diga o seu peso, apenas os numeros, em Kilos')
        peso = self.ouvir()
        self.falar('Diga a sua altura, apenas os numeros, em metros')
        altura = self.ouvir()
        self.falar(obj.calculo_imc(altura, peso))

    # Implementado / no menu
    def reproduzir_audio(self):
        obj = TocarMusica()
        obj.tocar_musica()

    def ver_imagem(self):
        obj = VerImagem()
        obj.visualizar_imagem()

    # Implementado / no menu
    def conversao_dolar(self, valor):
        obj = ConversaoDolar()
        convertido = obj.conversao_dolar(valor)
        self.falar(convertido)

    # Implementado / no menu
    def cotacao(self):
        obj = Cotacao()
        texto = obj.cotacao_dolar()
        self.falar(texto)

    def adicionar_na_agenda(self, evento):
        obj = Agenda()
        retorno = obj.escrever_agenda(evento)
        self.falar(retorno)

    def ler_agenda(self):
        obj = Agenda()
        eventos = obj.ler_agenda()
        for evento in eventos:
            self.falar(evento)

    def menu(self, mensagem):
        match mensagem:

            case 'previsão do tempo':
                self.falar('Ok, fale qual a cidade que você deseja saber o tempo')
                local = self.ouvir()
                self.previsao_tempo(local)

            case 'converter dinheiro':
                self.falar('Ok, vamos converter o seu dinheiro, informe a quantidade em reais')
                valor = self.ouvir()
                self.conversao_dolar(valor)

            case 'tocar música':
                self.falar('Ok, vou reproduzir o áudio')
                self.reproduzir_audio()

            case 'ver cotação':
                self.falar('Ok, vou falar a cotação do dolar de hoje')
                self.cotacao()

            case 'hora atual':
                self.falar('Ok, vou olhar a hora')
                self.falar_hora()

            case 'ler agenda':
                self.falar('Ok, vou ler os eventos da agenda')
                self.ler_agenda()

            case 'adicionar na agenda':
                self.falar('Diga o evento que você deseja adicionar na agenda')
                evento = self.ouvir()
                self.adicionar_na_agenda(evento)

            case 'imc':
                self.falar('Ok, vamos calcular o seu imc')
                self.imc()

            case 'ver imagem':
                self.falar('Abrindo imagem...')
                self.ver_imagem()

            case 'calcular':
                self.falar('Ok, vamos calcular...')
                self.falar('Fale o valor 1')
                valor1 = self.ouvir()

                self.falar('Fale o valor 2')
                valor2 = self.ouvir()
                self.calculadora(valor1, valor2)
