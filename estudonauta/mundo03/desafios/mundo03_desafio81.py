lista = []
while True:
    num = int(input('Digite um numero inteiro: '))
    lista.append(num)
    continuar = input('Deseja inserir mais um numero [S/N]? ')
    while continuar.lower() != 's' and continuar.lower() != 'n':
        print('Opcao invalida!')
        continuar = input('Deseja inserir mais um numero [S/N]? ')
    if continuar.lower() == 'n':
        break
print(f'{len(lista)} valores foram digitados.')
lista_decrescente = lista[:]
lista_decrescente.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista_decrescente}')
if lista.count(5) == 0:
    print('O valor cinco nao foi digitado.')
elif lista.count(5) == 1:
    print(f'O valor cinco foi digitado 1 vez.')
else:
    print(f'O valor 5 foi digitado {lista.count(5)} vezes nas posicoes ', end='')
    for c, v in enumerate(lista):
        if v == 5:
            print(f'{c} ', end='')