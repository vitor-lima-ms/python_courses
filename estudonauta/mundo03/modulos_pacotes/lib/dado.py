def validacao(valor):
    if (str(valor)[:1]).isnumeric() == True:
        return float(valor)
    while (str(valor)[:1]).isnumeric() == False:
        print('Opcao invalida!')
        valor = input('Digite um preco: R$').replace(',', '.').strip()
    return float(valor)