#Funcao
def escreva(texto):
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))


#Programa principal
while True:
    texto_usuario = input('Qual mensagem voce deseja exibir? ')
    escreva(texto_usuario)
    continuar = input('Deseja exibir outra mensagem [S/N]? ')
    while continuar.lower() != 's' and continuar.lower() != 'n':
        print('Opcao invalida!')
        continuar = input('Deseja exibir outra mensagem [S/N]? ')
    if continuar.lower() == 'n':
        break