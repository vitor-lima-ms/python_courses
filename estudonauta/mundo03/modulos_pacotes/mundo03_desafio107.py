import moeda
valor = float(input('Digite um valor: R$'))
print(f'A metade de {valor} e {moeda.metade(valor)}.')
print(f'O dobro de R${valor} e {moeda.dobro(valor)}.')
print(f'Aumentando 10% em {valor}, temos {moeda.aumento(valor)}.')
print(f'Diminuindo 13& em {valor}, temos {moeda.reducao(valor)}.')