from time import sleep
import menu
def visualizarcadastros():
    print('-' * len('PESSOAS CADASTRADAS'))
    print('PESSOAS CADASTRADAS')
    print('-' * len('PESSOAS CADASTRADAS'))
    cadastros = open('/home/vitor/estudonauta_python/mundo03/desafio_final/cadastros.txt')
    contador = 0
    pessoas = []
    for linha in cadastros:
        if contador == 0:
            contador += 1
            continue
        else:
            nome_idade = linha.replace('\n', '').split(',')
            pessoas.append(nome_idade)
    for pessoa in pessoas:
        print(f'{pessoa[0]}: {pessoa[1]} anos')
    sleep(5)
    menu.menu()