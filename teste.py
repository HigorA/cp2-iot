import requests
from bs4 import BeautifulSoup

cidade = input("Qual cidade você gostaria de saber a previsão do tempo, mestre?")
key = 'f0b1f4e7c14e0518dac3d664f119aaf5'
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=f0b1f4e7c14e0518dac3d664f119aaf5&lang=pt_br"

req = requests.get(link)
requisi = req.json()

print(requisi)

