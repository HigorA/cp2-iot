from sexta_feira import SextaFeira

obj = SextaFeira()
texto = obj.ouvir()

mensagem = 'ok mestre'
if texto == 'ok sexta-feira':
    obj.falar(mensagem)
    print(mensagem)



