class IMC:

    def __init__(self):
        pass

    def calculo_imc(self, altura, peso):
        imc = peso / (altura * altura)

        return f'O seu IMC é {imc}'

