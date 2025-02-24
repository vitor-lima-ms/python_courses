from random import randint
from time import sleep
dicionario_aux = {}
lista_jogadores = []
lista_resultados = []
lista_ordenada = []
for n_jogador in range(0, 4):
    dicionario_aux['Jogador'] = n_jogador + 1
    dicionario_aux['Dado'] = randint(1, 6)
    lista_jogadores.append(dicionario_aux.copy())
    dicionario_aux.clear()
for jogador in lista_jogadores:
    sleep(1)
    print(f'O jogador {jogador["Jogador"]} jogou {jogador["Dado"]}')
    lista_resultados.append(jogador['Dado'])
lista_resultados.sort()
for resultado in lista_resultados:
    for jogador in lista_jogadores:
        if jogador in lista_ordenada:
            continue
        elif resultado == jogador['Dado']:
            lista_ordenada.append(jogador)
contador = 1
sleep(0.5)
print(('-' *5), end='')
print('Resultado final!', end='')
print(('-' *5))
for ordem in range((len(lista_ordenada) + 1), 1, -1):
    sleep(0.5)
    print(f'{contador}o lugar: Jogador {lista_ordenada[ordem - 2]["Jogador"]} com {lista_ordenada[ordem - 2]["Dado"]}')
    contador += 1