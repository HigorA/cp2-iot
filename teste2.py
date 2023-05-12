import requests
from bs4 import BeautifulSoup

cidade = input("Qual cidade você gostaria de saber a previsão do tempo, metre?")
procura = f"A previsão do tempo em {cidade} é de:"
url = f"https://www.google.com/search?q={procura}"
req = requests.get(url)
l = BeautifulSoup(req.text, "html.parser")
up = l.find("div", class_="BNeawe").text

tex1 = (procura + up)
print(tex1)