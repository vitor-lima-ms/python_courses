tupla = (int(input('Digite o primeiro numero: ')),
         int(input('Digite o primeiro numero: ')),
         int(input('Digite o primeiro numero: ')),
         int(input('Digite o primeiro numero: ')))
cont_9 = 0
cont_3 = 0
pos_3 = 0
lista_par = []
for i in tupla:
    if i == 9:
        cont_9 += 1
    elif i == 3:
        cont_3 += 1
        pos_3 = tupla.index(3)
    elif i % 2 == 0:
        lista_par.append(i)
if cont_9 == 0:
    print('O valor 9 nao foi digitado nenhuma vez.')
elif cont_9 == 1:
    print('O valor 9 foi digitado 1 vez.')
else:
    print(f'O valor 9 foi digitado {cont_9} vezes.')
if cont_3 == 0:
    print(f'O valor 3 nao foi digitado nenhuma vez.')
else:
    print(f'O valor 3 aparece pela primeira vez na {pos_3 + 1} posicao.')
if lista_par is None:
    print('Nenhum numero par foi digitado')
else:
    print(f'Os valores pares digitados foram {lista_par}.')