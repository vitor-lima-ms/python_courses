import leiaint.leiaint_idade as age
import menu
def novocadastro():
    cadastros = open('/home/vitor/estudonauta_python/mundo03/desafio_final/cadastros.txt', 'a')
    while True:
        nome = input('NOME: ')
        cadastros.write(f'\n{nome}')
        idade = age.leiaint(input('IDADE: '))
        cadastros.write(str(f',{idade}'))
        continuar = input('DESEJA CADASTRAR MAIS ALGUÉM [S/N]? ')
        while continuar.lower() != 's' and continuar.lower() != 'n':
            print('OPÇÃO INVÁLIDA!')
            continuar = input('DESEJA CADASTRAR MAIS ALGUÉM [S/N]? ')
        if continuar.lower() == 'n':
            break
    menu.menu()