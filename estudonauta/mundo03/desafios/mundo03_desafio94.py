from time import sleep
dicionario_aux = {}
lista_pessoas = []
cont_pessoas = 0
soma_idades = 0
while True:
    dicionario_aux['Nome'] = input('Nome: ')
    dicionario_aux['Sexo'] = input('Sexo [M/F]: ')
    while dicionario_aux['Sexo'].lower() != 'm' and dicionario_aux['Sexo'].lower() != 'f':
        print('Opcao invalida!')
        dicionario_aux['Sexo'] = input('Sexo [M/F]: ')
    dicionario_aux['Idade'] = int(input('Idade: '))
    cont_pessoas += 1
    soma_idades += dicionario_aux['Idade']
    lista_pessoas.append(dicionario_aux.copy())
    dicionario_aux.clear()
    continuar = input('Deseja cadastrar mais alguem [S/N]? ')
    while continuar.lower() != 's' and continuar.lower() != 'n':
        print('Opcao invalida!')
        continuar = input('Deseja cadastrar mais alguem [S/N]? ')
    if continuar.lower() == 'n':
        break
sleep(1)
print('Calculando...')
sleep(0.5)
print(f'No total, foram {cont_pessoas} pessoas cadastradas.')
print(f'A media de idade do grupo e: {soma_idades / cont_pessoas}')
lista_mulheres = []
for pessoa in lista_pessoas:
    if pessoa['Sexo'].lower() == 'f':
        lista_mulheres.append(pessoa['Nome'])
print(f'As mulheres cadastradas foram: {lista_mulheres}')
lista_idade_maior_media = []
for pessoa in lista_pessoas:
    if pessoa['Idade'] > (soma_idades / cont_pessoas):
        lista_idade_maior_media.append(pessoa['Nome'])
print(f'As pessoas com idade acima da media do grupo sao: {lista_idade_maior_media}')