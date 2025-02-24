import menu_opcoes
def leiaint(valor):
    try:
        return int(valor)
    except:
        menu_opcoes.opcoes()
        print('ERRO!')
        valor = input('OPÇÃO: ')
        while str(valor).strip().isnumeric() == False:
            menu_opcoes.opcoes()
            print('ERRO!')
            valor = input('OPÇÃO: ')
        return int(valor)