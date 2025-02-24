#Funcao
def ficha(nome='', gols=''):
    if nome.strip() == '':
        nome = 'Desconhecido'
    if gols.isnumeric() == False:
        gols = '0'
    return nome, gols


#Programa principal
nome_jogador = input('Nome do jogador: ')
numero_gols = input('Quantidade de gols marcados: ')
resultado = ficha(nome_jogador, numero_gols)
print(f'O jogador {resultado[0]} fez {resultado[1]} gol(s) no campeonato!')