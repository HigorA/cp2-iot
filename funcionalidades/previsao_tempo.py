import requests
from bs4 import BeautifulSoup


class PrevisaoTempo:

    def __init__(self):
        pass

    def previsao(self, local):
        procura = f"A previsão do tempo em {local} é de:"
        url = f"https://www.google.com/search?q={procura}"
        req = requests.get(url)
        l = BeautifulSoup(req.text, "html.parser")
        up = l.find("div", class_="BNeawe").text
        return procura + ' ' + up

