def formatacao(valor):
    valor_novo = f'{valor:.2f}'
    formatado = str(valor_novo).replace('.', ',')
    formatado = 'R$' + formatado
    return formatado
def aumento(valor, formatar=False):
    if formatar == False:
        return 1.1 * valor
    elif formatar == True:
        return formatacao(1.1 * valor)
def reducao(valor, formatar=False):
    if formatar == False:
        return 0.87 * valor
    elif formatar == True:
        return formatacao(0.87 * valor)
def metade(valor, formatar=False):
    if formatar == False:
        return valor / 2
    elif formatar == True:
        return formatacao(valor / 2)
def dobro(valor, formatar=False):
    if formatar == False:
        return valor * 2
    elif formatar == True:
        return formatacao(valor * 2)
def resumo(valor, aumento, reducao):
    print('-' * (len('RESUMO DO VALOR')))
    print('RESUMO DO VALOR')
    print('-' * (len('RESUMO DO VALOR')))
    print(f'Preco analisado: {formatacao(float(valor))}')
    print(f'Dobro do preco: {formatacao(float(valor) * 2)}')
    print(f'Metade do preco: {formatacao(float(valor) / 2)}')
    print(f'{aumento}% de aumento: {formatacao(float(valor) * (1 + (aumento / 100)))}')
    print(f'{reducao}% de reducao: {formatacao(float(valor) * (1 - (reducao / 100)))}')