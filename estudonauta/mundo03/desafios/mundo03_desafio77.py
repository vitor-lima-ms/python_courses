tupla = ('aprender', 'programar', 'linguagem', 'python')
for palavra in tupla:
    vogais = ''
    for letra in palavra:
        if letra in 'aeiou':
            vogais += letra
    if len(vogais) == 0:
        print(f'A palavra {palavra} nao tem vogais.')
    elif len(vogais) == 1:
        print(f'A palavra {palavra} tem a vogal {vogais}.')
    else:
        print(f'A palavra {palavra} tem as vogais {vogais}.')


