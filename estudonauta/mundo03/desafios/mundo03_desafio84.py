main_list = []
aux_list =[]
cont_pessoas = 0
menor_peso = 0
maior_peso = 0
while True:
    nome = input('Nome: ')
    aux_list.append(nome)
    peso = float(input('Peso (Kg): '))
    if cont_pessoas == 0:
        menor_peso = maior_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
    aux_list.append(peso)
    main_list.append(aux_list[:])
    aux_list.clear()
    cont_pessoas += 1
    continuar = input('Deseja cadastrar mais alguma pessoa [S/N]? ')
    while continuar.lower() != 'n' and continuar.lower() != 's':
        print('Opcao invalida!')
        continuar = input('Deseja cadastrarmais alguma pessoa [S/N]? ')
    if continuar.lower() == 'n':
        break
pessoas_maior_peso = []
pessoas_menor_peso = []
for pessoa in main_list:
    if pessoa[1] == maior_peso:
        pessoas_maior_peso.append(pessoa[0])
    elif pessoa[1] == menor_peso:
        pessoas_menor_peso.append(pessoa[0])
print(f'No total, foram {cont_pessoas} pessoas cadastradas.')
print(f'Pessoas com o menor peso ({menor_peso}): {pessoas_menor_peso}.')
print(f'Pessoas com o menor peso ({maior_peso}): {pessoas_maior_peso}.')