lista = []
for i in range(0, 5):
    num = int(input(f'Digite o {i+ 1} numero inteiro: '))
    if i == 0:
        lista.append(num)
    elif i > 0:
        if len(lista) == 1:
             if num < lista[0]:
                lista.insert(0, num)
             elif num > lista[0]:
                lista.insert(1, num)
        elif len(lista) > 1:
            if num < min(lista):
                lista.insert(0, num)
            elif num > max(lista):
                lista.insert((len(lista)), num)
            else:
                for numero in lista:
                    if num > numero:
                        continue
                    elif num == numero:
                        lista.insert(lista.index(numero), num)
                        break
                    elif num < numero:
                        lista.insert(lista.index(numero), num)
                        break
print(f'Valores digitados em ordem crescente: {lista}')