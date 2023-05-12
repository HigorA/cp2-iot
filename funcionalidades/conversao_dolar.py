import re
import requests


class ConversaoDolar:

    def __init__(self):
        pass


    def conversao_dolar(self, valor_reais):
        padrao = r"\d+\,\d+|\d+\.\d+|\d+"
        numeros = re.findall(padrao, valor_reais)

        if numeros:
            numero = int(numeros[0])
            print(numero)
            response = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
            cotacao = float(response.json()["USD"]["high"])

            valor_dolar = numero / cotacao

            print(f"{numero} reais equivale a {valor_dolar:.2f} dolar")
            return f"{numero} reais equivale a {valor_dolar:.2f} dólares"
        else:
            print("O valor que você informou não é valido.")
            return "O valor que você informou não é valido."

