lista = []
while True:
    num = int(input('Digite um numero inteiro: '))
    if lista.count(num) == 0:
        lista.append(num)
    else:
        print('Valor ja existente. Nao vou adicionar!')
    continuar = input('Deseja continuar [S/N]? ')
    while continuar.lower() != 's' and continuar.lower() != 'n':
        print('Valor invalido!')
        continuar = input('Deseja continuar [S/N]? ')
    if continuar.lower() == 's':
        continue
    elif continuar.lower() == 'n':
        break
lista.sort()
print(f'Voce digitou os numeros {lista}.')