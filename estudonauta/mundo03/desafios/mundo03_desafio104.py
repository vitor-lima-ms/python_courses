#Funcao
def leiaint(entrada):
    """Funcao que verifica se uma entrada e um numero inteiro.
    :param entrada: A entrada fornecida pelo usuario.
    :return: Retorna o valor caso este seja numerico"""
    numero = 0
    while True:
        if entrada.isnumeric():
            numero = int(entrada)
            break
        else:
            print('ERRO! Digite um numero inteiro.')
            entrada = input('Digite um numero: ')
    return numero


#Programa princial
entrada_usuario = leiaint(input('Digite um numero: '))
print(f'Vc digitou o numero inteiro {entrada_usuario}')