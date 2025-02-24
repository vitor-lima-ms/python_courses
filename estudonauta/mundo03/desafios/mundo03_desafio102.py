#Funcao
def fatorial(numero, mostrar=False):
    """Calcula o fatorial de um numero.
    :param numero: O numero para o qual sera calculado o fatorial
    :param mostrar (Opcional): Exibe o processo de calculo juntamente com o resultado
    :return: """
    fat = 1
    if mostrar == False:
        for numeros in range(2, (numero + 1)):
            fat *= numeros
        return fat
    elif mostrar == True:
        lista_fatorial = []
        for numeros in range(2, (numero + 1)):
            lista_fatorial.append(numeros)
            fat *= numeros
        lista_fatorial.append(fat)
        return lista_fatorial


#Programa principal
numero_fatorial = int(input('Para qual numero vc deseja que eu calcule o fatorial? '))
mostrar_usuario = input('Deseja que o processo seja apresentado na tela [S/N]? ')
while mostrar_usuario.lower() != 's' and mostrar_usuario.lower() != 'n':
    print('Opcao invalida!')
    mostrar_usuario = input('Deseja que o processo seja apresentado na tela [S/N]? ')
if mostrar_usuario.lower() == 'n':
    resultado = fatorial(numero_fatorial)
    print(f'O fatorial de {numero_fatorial} e {resultado}.')
else:
    resultado = fatorial(numero_fatorial, True)
    print('1 X ', end='', flush=True)
    for indice in range(0, len(resultado)):
        if indice == (len(resultado) - 2):
            print(f'{resultado[indice]} ', end='', flush=True)
            continue
        if indice == (len(resultado) - 1):
            print(f'= {resultado[indice]}')
            break
        print(f'{resultado[indice]} X ', end='', flush=True)
    print(f'O fatorial de {numero_fatorial} e {resultado[len(resultado) - 1]}.')
help(fatorial)