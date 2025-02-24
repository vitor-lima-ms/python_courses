import menu_opcoes
import leiaint.leiaint_opcao as op
import novo_cadastro
import visualizar_cadastros
def menu():
    menu_opcoes.opcoes()
    opcao = op.leiaint(input('OPÇÃO: '))
    while opcao < 1 or opcao > 3:
        menu_opcoes.opcoes()
        print('ERRO!')
        opcao = op.leiaint(input('OPÇÃO: '))
    if opcao == 1:
        novo_cadastro.novocadastro()
    elif opcao == 2:
        visualizar_cadastros.visualizarcadastros()
    elif opcao == 3:
        print('ATÉ MAIS!')