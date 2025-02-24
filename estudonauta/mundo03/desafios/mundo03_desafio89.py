main_list = []
aux1 = []
aux2 = []
while True:
    nome = input('Nome: ')
    aux1.append(nome)
    nota1 = float(input('Nota 1: '))
    aux2.append(nota1)
    nota2 = float(input('Nota 2: '))
    aux2.append(nota2)
    aux1.append(aux2[:])
    main_list.append(aux1[:])
    aux1.clear()
    aux2.clear()
    print(main_list)
    continuar = input('Deseja continuar [S/N]? ')
    while continuar.lower() != 'n' and continuar.lower() != 's':
        print('Opcao invalida!')
        continuar = input('Deseja continuar [S/N]? ')
    if continuar.lower() == 'n':
        break
for i in range(0, len(main_list)):
    print(f'ID: {i}', end='    ')
    print(f'Nome: {main_list[i][0]}', end='    ')
    aux3 = 0
    for j in range(0, 2):
        aux3 += main_list[i][1][j]
    media = aux3 / 2
    print(f'Media: {media}')
mostrar = int(input(f'Deseja mostrar as notas de qual aluno (999 para parar)? '))
while mostrar not in range(0, len(main_list)) and mostrar != 999:
        print('Opcao invalida!')
        mostrar = int(input(f'Deseja mostrar as notas de qual aluno (999 para parar)? '))
while True:
    if mostrar == 999:
        break
    print(f'Notas de {main_list[mostrar][0]}: {main_list[mostrar][1]}')
    mostrar = int(input(f'Deseja mostrar as notas de qual aluno (999 para parar)? '))
    while mostrar not in range(0, len(main_list)) and mostrar != 999:
        print('Opcao invalida!')
        mostrar = int(input(f'Deseja mostrar as notas de qual aluno (999 para parar)? '))
