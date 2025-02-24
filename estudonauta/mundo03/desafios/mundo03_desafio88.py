from random import randint
from time import sleep
qtd_jogos = int(input('Quantos jogos vc quer que eu sorteie? '))
for i in range(0, qtd_jogos):
    jogo = []
    for j in range(0, 6):
        num = randint(1, 60)
        if j == 0:
            jogo.append(num)
            continue
        elif jogo.count(num) == 1:
            num = randint(1, 60)
            jogo.append(num)
            while jogo.count(num) > 1:
                jogo.pop()
                num = randint(1, 60)
                jogo.append(num)
        else:
            jogo.append(num)
    sleep(1)
    print(f'Jogo {i + 1}: {jogo}')