from datetime import datetime
ano_atual = int(datetime.today().strftime('%Y'))
#Funcao
def voto(ano_nascimento):
    idade = ano_atual - ano_nascimento
    if (ano_atual - ano_nascimento) < 16:
        return 'impedido', idade
    elif 16 <= (ano_atual - ano_nascimento) < 18:
        return 'opcional', idade
    elif 18 <= (ano_atual - ano_nascimento) < 65:
        return 'obrigatorio', idade
    else:
        return 'opcional', idade


#Programa principal
resposta = voto(int(input('Ano de nascimento: ')))
print(f'Com {resposta[1]} anos o voto e {resposta[0]}')