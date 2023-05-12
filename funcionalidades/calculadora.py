class Calculadora:

    def __init__(self, valor1, valor2):
        if isinstance(valor1, str) or isinstance(valor2, str):
            pass
        self.valor1 = float(valor1)
        self.valor2 = float(valor2)

    def calcular(self, operacao):
        if operacao == 'somar' or operacao == 'adicionar' or operacao == 'adição':
            return self.adicao()
        elif operacao == 'menos' or operacao == 'subtrair' or operacao == 'subtração':
            return self.subtrair()
        elif operacao == 'multiplicar' or operacao == 'vezes':
            return self.multiplicar()
        elif operacao == 'dividir':
            return self.dividir()
        else:
            return 'operação inválida'

    def adicao(self):
        return f'{self.valor1 + self.valor2}'

    def subtrair(self):
        return f'{self.valor1 - self.valor2}'

    def multiplicar(self):
        return f'{self.valor1 * self.valor2}'

    def dividir(self):
        return f'{self.valor1/ self.valor2}'

