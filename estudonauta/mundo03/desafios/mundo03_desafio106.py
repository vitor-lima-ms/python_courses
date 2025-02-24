from time import sleep
def pyhelp(comando):
    print('-' * len(f'Acessando o menu do comando {comando}'))
    print(f'Acessando o menu do comando {comando}')
    print('-' * len(f'Acessando o menu do comando {comando}'))
    sleep(2)
    return help(comando)

comando_usuario = input('Funcao o bibli: ')
retorno = pyhelp(comando_usuario)
while comando_usuario.lower() != 'fim':
    pyhelp(input('Funcao ou biblioteca: '))