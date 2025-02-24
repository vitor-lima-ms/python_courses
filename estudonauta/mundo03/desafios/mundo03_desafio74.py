from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = 0
menor = 0
for i in range(0, len(tupla)):
    num = tupla[i]
    if i == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'O maior numero sorteado foi {maior}')
print(f'O menor numero sorteado foi {menor}')