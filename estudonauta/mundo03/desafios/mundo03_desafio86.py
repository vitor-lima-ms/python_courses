matriz = [[], [], []] #Cada [] representa uma linha. Cada elemento nesse [] representa o valor q sera colocado em uma coluna dessa linha
for linha in range(0, len(matriz)):
    for coluna in range(0, 3): #Como queremos uma matriz 3x3
        num = int(input(f'Digite um valor inteiro para a posicao [{linha}, {coluna}]: '))
        matriz[linha].append(num)
print(('-' * 5), end='')
print('MATRIZ', end='')
print(('-' * 5))
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')