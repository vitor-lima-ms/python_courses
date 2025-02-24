def leiaint(valor):
    try:
        if str(valor).strip() == '':
            print('O usuario prefiriu nao digitar um valor.')
            return 0
        return int(valor)
    except:
        print('ERRO!')
        valor = input('Digite um numero inteiro: ')
        if str(valor).strip() == '':
            print('O usuario prefiriu nao digitar um valor.')
            return 0
        while str(valor).strip().isnumeric() == False:
            print('ERRO!')
            valor = input('Digite um numero inteiro: ')
            if str(valor).strip() == '':
                print('O usuario prefiriu nao digitar um valor.')
                return 0
        return int(valor)