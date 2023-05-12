class Agenda:

    def __init__(self):
        pass

    def ler_agenda(self):
        agenda = open('agenda.txt', 'r')
        conteudo = agenda.readlines()
        agenda.close()
        return conteudo

    def escrever_agenda(self, evento):
        agenda = open('agenda.txt', 'a')
        agenda.write(evento)
        agenda.close()
        return 'Evento adicionado com sucesso!'

