matriz = [[], [], []] #Cada [] representa uma linha. Cada elemento nesse [] representa o valor q sera colocado em uma coluna dessa linha
soma_par = 0
for linha in range(0, len(matriz)):
    for coluna in range(0, 3): #Como queremos uma matriz 3x3
        num = int(input(f'Digite um valor inteiro para a posicao [{linha}, {coluna}]: '))
        if num % 2 == 0:
            soma_par += num
        matriz[linha].append(num)
print(('-' * 5), end='')
print('MATRIZ', end='')
print(('-' * 5))
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')
print(f'A soma de todos os valores pares digitados e: {soma_par}')
print(f'A soma dos valores da terceira coluna e: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')