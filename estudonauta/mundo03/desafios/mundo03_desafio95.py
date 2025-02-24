dicionario_aux = {}
lista_aux = []
lista_final = []
while True:
    dicionario_aux['Nome'] = input('Nome de jogador: ')
    partidas = int(input(f'Quantas partidas {dicionario_aux["Nome"]} jogou? '))
    dicionario_aux['Partidas'] = partidas
    for partida in range(0, partidas):
        gols = int(input(f'Quantos gols {dicionario_aux["Nome"]} fez na {partida + 1}a partida? '))
        lista_aux.append(gols)
    dicionario_aux['Gols em cada partida'] = lista_aux[:]
    dicionario_aux['Total de gols'] = sum(lista_aux[:])
    lista_final.append(dicionario_aux.copy())
    dicionario_aux.clear()
    lista_aux.clear()
    continuar = input('Deseja continuar [S/N]? ')
    while continuar.lower() != 's' and continuar.lower() != 'n':
        print('Opcao invalida!')
        continuar = input('Deseja continuar [S/N]? ')
    if continuar.lower() == 'n':
        break
cont = 0
for jogador in lista_final:
    print(f'ID = {cont}    ', end='')
    print(f'Nome = {jogador["Nome"]}    ', end='')
    print(f'Partidas = {jogador["Partidas"]}    ', end='')
    print(f'Gols = {jogador["Gols em cada partida"]}    ', end='')
    print(f'Total de gols = {jogador["Total de gols"]}')
    cont += 1
while True:
    mostrar = int(input('Deseja mostrar os dados detalhados de qual jogador [999 para parar]? '))
    if mostrar == 999:
        break
    while mostrar < 0 or (mostrar > cont and mostrar != 999):
        print('Opcao invalida!')
        mostrar = int(input('Deseja mostrar os dados detalhados de qual jogador [999 para parar]? '))
    if mostrar == 999:
        break
    print(f'Levantamento de dados do jogador {lista_final[mostrar]["Nome"]}')
    for partida in range(0, lista_final[mostrar]['Partidas']):
        print(f'Na partida {partida + 1}, {lista_final[mostrar]["Nome"]} fez {lista_final[mostrar]["Gols em cada partida"][partida]} gols')