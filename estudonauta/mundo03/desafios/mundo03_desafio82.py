lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input(f'Digite um numero inteiro: '))
    lista.append(num)
    continuar = input('Deseja inserir mais um numero [S/N]? ')
    while continuar.lower() != 's' and continuar.lower() != 'n':
        print('Opcao invalida!')
        continuar = input('Deseja inserir mais um numero [S/N]? ')
    if continuar.lower() == 'n':
        break
for numero in lista:
    if (numero % 2) == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
print(f'Lista completa: {lista}.')
if lista_par == []:
    print('Nenhum numero par foi digitado.')
else:
    print(f'Lista apenas com numeros pares: {lista_par}.')
if lista_impar == []:
    print('Nenhum numero impar foi digitado.')
else:
    print(f'Lista apenas com numeros impares: {lista_impar}.')