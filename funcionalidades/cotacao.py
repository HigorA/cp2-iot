import requests


class Cotacao:

    def __init__(self):
        pass

    def cotacao_dolar(self):
        response = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
        cotacao = float(response.json()["USD"]["high"])
        print(f'{cotacao:.2f}')
        return f'A cotação do Dolar atualmente está em {cotacao:.2f} dolares'

