from time import sleep
#Funcao
def valor_maximo(*numeros):
    print('Analisando valores...')
    sleep(1.5)
    maior = 0
    for numero in numeros:
        sleep(1)
        print(numero, end=' ', flush=True)
        if numero > maior:
            maior = numero
    sleep(0.5)
    print(f'Ao todo, foram analisados {len(numeros)} numeros.')
    sleep(0.5)
    print(f'O maior valor informado foi {maior}.')


#Programa principal
valor_maximo(2, 9, 4, 5, 7, 1)
valor_maximo(4, 7, 0)
valor_maximo(1, 2)
valor_maximo(6)
valor_maximo()
