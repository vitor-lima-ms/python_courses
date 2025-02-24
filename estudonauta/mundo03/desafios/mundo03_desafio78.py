numeros = []
for i in range(0,5):
    numeros.append(int(input(f'Digite o {i + 1} numero inteiro: ')))
if max(numeros) == min(numeros):
    print('Os valores digitados sao todos iguais!')
else:
    print(f'O maior valor digitado foi {max(numeros)}, nas posicoes: ', end='')
    for c, v in enumerate(numeros):
        if v == max(numeros):
            print(f'{c} ', end='')
    print(f'\nO menor valor digitado foi {min(numeros)}, nas posicoes: ', end='')
    for c, v in enumerate(numeros):
        if v == min(numeros):
            print(f'{c} ', end='')