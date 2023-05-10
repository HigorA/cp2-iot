from sexta_feira import SextaFeira

obj = SextaFeira()
texto = obj.ouvir()

mensagem = 'ok mestre, o que deseja fazer agora?'
if texto == 'ok sexta-feira':
    obj.falar(mensagem)
    print(mensagem)

    escolha = obj.ouvir()
    print(escolha)
    obj.menu(escolha)

