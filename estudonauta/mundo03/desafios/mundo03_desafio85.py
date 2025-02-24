lista = [[], []]
for i in range(0, 7):
    num = int(input(f'Digite {i + 1}o numero inteiro: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Lista de numeros pares em ordem crescente: {lista[0]}.')
print(f'Lista de numeros impares em ordem crescente: {lista[1]}.')