#Semelhantes as tuplas, mas sao mutaveis
lista = ['a', 'b', 'c', 'd']
print(lista[0])

lista[0] = 'e' #Podemos mudar os valores da lista sem interromper o codigo
print(lista[0])

lista.append('f') #Adiciona elementos no final da lista
print(lista)

lista.insert(0, 'a') #Adiciona um elemento no indice especificado
print(lista)

#Formas de remover elementos
del(lista[1]) #Remove pelo indice
print(lista)
lista.pop(0) #Normalmente utilizado para remover o ultimo elemento, mas tambem podemos passar um indice
print(lista)
lista.pop()
print(lista)
lista.remove('e') #Remove pelo conteudo. Se o elemento aparecer mais de uma vez, remove so a primeira ocorrencia
print(lista)

if 'c' in lista: #Verifica se o elemento exitse na lista
    lista.remove('c')
else:
    print('A letra c nao esta na lista')
print(lista)

#Criando listas
lista = list(range(4, 11)) #Utilizando o range
print(lista)
lista = list(range(4, 11, 2)) #O ultimo argumento determina o intervalo entre os elementos da lista
print(lista)

lista = []
for i in range(0, 5):
    lista.append(int(input('Digite um numero inteiro: ')))
print(lista)

x = list()
print(x)

#Organizando listas
lista = ['a', 'f', 'b', 'i', 'y']
print(lista)
lista.sort() #Ordenacao crescente -> Muda a lista
print(lista)

lista = ['a', 'f', 'b', 'i', 'y']
print(lista)
lista.sort(reverse=True) #Ordenacao decrescente -> Muda a lista
print(lista)

#Tamanho de uma lista
lista = ['a', 'f', 'b', 'i', 'y']
print(len(lista))

#Mostrando elementos de uma lista
lista = []
lista.append(1)
lista.append(2)
lista.append(3)
print(lista)
for i in range(0, len(lista)):
    print(f'{lista[i]}')
for valor in lista:
    print(f'O valor e {valor}')
for posicao, valor in enumerate(lista): #enumerate tambem funciona para listas
    print(f'O valor e {valor} e esta na posicao {posicao}')

#
a = [1, 2, 3, 4]
b = a
print(f'Lista a: {a}')
print(f'Lista b: {b}')

a = [1, 2, 3, 4]
b = a
b[0] = 5
print(f'Lista a: {a}')
print(f'Lista b: {b}')
#Mesmo alterando o elemento na lista b, a lista a tambem e alterada
#Essa atribuicao nao cria uma copia, mas sim uma interligacao

#Copias
a = [1, 2, 3, 4]
b = a[:] #Forma de criar copia. Como e com slicing, podemos criar uma copia apenas com valores desejados
b[0] = 5
print(f'Lista a: {a}')
print(f'Lista b: {b}')
#Dessa forma, alteracoes em b nao afetam a

#Maior e menor valor
a = [4, 5, 4, 4, 9, 9]
print(max(a)) #Maior valor de uma lista
print(min(a)) #Menor valor de uma lista
'''Os metodos de tupla sao validos para listas'''

#Listas dentro de listas
a = [1, 2, 3]
b = [4, 5, 6]
a.append(b[:])
print(a)
print(a[3][0])

lista = []
aux = [] #Estrutura auxiliar para armazenar dados e coloca-los na lista principal
for i in range(0, 3):
    aux.append(input('Nome: '))
    aux.append(int(input('Idade: ')))
    lista.append(aux[:])
    aux.clear()