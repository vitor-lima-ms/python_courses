'''A resolucao baseia-se no conceito de remover o ultimo parenteses aberto da lista sempre quando seu correspondente
for encontrado. O ultimo parenteses aberto sempre e o primeiro a ser fechado'''
exp = str(input('Digite uma expressao com parenteses: '))
lista = []
for caractere in exp:
    if caractere == '(':
        lista.append(caractere)
    elif caractere == ')':
        if len(lista) > 0:
            lista.pop()
        elif len(lista) == 0:
            lista.append(caractere)
if len(lista) == 0:
    print('Expressao valida')
elif len(lista) > 0:
    print('Expressao invalida')