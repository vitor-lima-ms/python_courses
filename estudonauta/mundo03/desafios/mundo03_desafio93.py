jogador_stats = {}
jogador_stats['Nome'] = input('Nome do bagre: ')
partidas = int(input(f'Quantas partidas {jogador_stats["Nome"]} jogou? '))
gols = []
for partida in range(0, partidas):
    gol = int(input(f'Quantos gols {jogador_stats["Nome"]} fez na {partida + 1}a partida? '))
    gols.append(gol)
jogador_stats['Gols'] = gols[:]
jogador_stats['Total'] = sum(gols[:])
print(('-' * 5), end='')
print('RESUMO DO BAGRE', end='')
print('-' * 5)
print(f'O jogador {jogador_stats["Nome"]} jogou {partidas} partidas e marcou um total de {jogador_stats["Total"]}')
for contador in range(0, partidas):
    print(f'Na {contador + 1}a partida marcou {gols[contador]}')
print('Hexa so em 2048 desse jeito!')