from datetime import datetime
cadastro = {}
ano_atual = int(datetime.today().strftime('%Y'))
cadastro['Nome'] = input('Nome: ')
ano_nascimento = int(input('Ano de nascimento: '))
cadastro['Idade'] = ano_atual - ano_nascimento
cadastro['CTPS'] = int(input('CTPS (Caso nao tenha, informar 0): '))
if cadastro['CTPS'] != 0:
    cadastro['Ano de contratacao'] = int(input('Ano de contratacao: '))
    cadastro['Salario'] = float(input('Salario (R$): '))
    cadastro['Ano de aposentadoria'] = cadastro['Ano de contratacao'] + 35
    cadastro['Idade de aposentadoria'] = cadastro['Ano de aposentadoria'] - ano_nascimento
for chave, valor in cadastro.items():
    print(f'{chave} = {valor}')