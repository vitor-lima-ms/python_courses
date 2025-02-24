def leiaint(valor):
    try:
        return int(valor)
    except:
        print('ERRO!')
        valor = input('IDADE: ')
        while str(valor).strip().isnumeric() == False:
            print('ERRO!')
            valor = input('IDADE: ')
        return int(valor)