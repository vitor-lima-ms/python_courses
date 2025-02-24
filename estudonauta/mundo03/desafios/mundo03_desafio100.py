from time import sleep
from random import randint
#Funcoes
def sorteia(lista):
    print('Sorteando os numeros...')
    sleep(1.5)
    for contador in range(0, 5):
        numero = randint(1, 10)
        print(f'{contador + 1}o numero sorteado: {numero}')
        sleep(1)
        lista.append(numero)

def soma_pares(lista):
    soma_par = 0
    for indice in range(0, len(lista)):
        if lista[indice] % 2 == 0:
            soma_par += lista[indice]
    sleep(1)
    print(f'A soma dos numeros pares sorteados e: {soma_par}')


#Programa principal
numeros = []
sorteia(numeros)
soma_pares(numeros)