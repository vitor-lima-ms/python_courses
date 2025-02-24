def leiafloat(valor):
    try:
        valor_substituido = str(valor).strip().replace(',', '.')
        if valor_substituido == '':
            print('O usuario prefiriu nao digitar um valor.')
            return 0
        while valor_substituido.isnumeric() == True:
            print('ERRO!')
            valor_substituido = input('Digite um numero com ponto flutuante: ').strip().replace(',', '.')
        return float(valor_substituido)
    except:
        while valor_substituido.replace('.', '').isdecimal() == False or valor_substituido.isnumeric() == True or valor_substituido.count('.') > 1:
            if valor_substituido == '':
                print('O usuario prefiriu nao digitar um valor.')
                return 0
            print('ERRO!')
            valor_substituido = input('Digite um numero com ponto flutuante: ').strip().replace(',', '.')            
        return float(valor_substituido)