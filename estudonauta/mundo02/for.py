#For

'''Estrutura de repetição com variável de controle'''

from time import sleep

#Exemplo 1

for i in range(0, 3): #Desconsidera segundo algarismo referente ao tamanho do intervalo
    print(i)

#Exemplo 2
    
for i in range (6, 0, -1): #-1 denota que a contagem é decrescente
    print(i)
    sleep(1)

#Exemplo 3
    
for i in range (0, 7, 2): #O último argumento denota o tamanho do 'passo' dado
    print(i)

#Exemplo 4
    
x = int(input('Digite um número inteiro: '))

for i in range(0, (x + 1)):
    print(i)

'''Podemos utilizar uma variável de entrada no laço.
o +1 é utilizado para que a contagem alcançe o
valor da variável de entrada'''

#Exemplo 5

inicio = int(input('Começa em: '))
final = int(input('Termina em: '))
passo = int(input('Com o passo de: '))

for i in range(inicio, (final + 1), passo):
    print(i)
    
#Exemplo 6

lista = []

for i in range(0, 3):
    x = int(input('Esse número vai ser adicionado à lista: '))
    lista.append(x)

print(lista)

#Exemplo 7

lista = ['Maçã', 'Banana', 'Café']

for i in range(0, len(lista)):
    item = lista[i]
    if item != 'Café':
        print('Ainda não achei o café :(')
        sleep(2)
    else:
        print('Achei o café!')

#Exemplo 8

soma = 0

for i in range(0, 4):
    n = int(input('Digite um número inteiro: '))
    soma = soma + n #Ou s += n

print(soma)