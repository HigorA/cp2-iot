from datetime import datetime


class VerHora:

    def __init__(self):
        pass

    def hora_atual(self):
        agora = datetime.now()
        hora_atual = agora.strftime("%H")
        minuto = agora.minute

        if int(hora_atual) > 12:
            print(f'Agora são {int(hora_atual) - 12} horas da tarde e {minuto} minutos!')
            return f'Agora são {int(hora_atual) - 12} horas da tarde e {minuto} minutos!'
        else:
            print(f'Agora são {hora_atual} horas da manhã e {minuto} minutos!')
            return f'Agora são {hora_atual} horas da manhã e {minuto} minutos!'

