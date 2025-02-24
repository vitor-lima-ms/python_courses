import moeda
valor = float(input('Digite um valor: R$'))
print(f'A metade de {moeda.formatacao(valor)} e {moeda.formatacao(moeda.metade(valor))}.')
print(f'O dobro de R${moeda.formatacao(valor)} e {moeda.formatacao(moeda.dobro(valor))}.')
print(f'Aumentando 10% em {moeda.formatacao(valor)}, temos {moeda.formatacao(moeda.aumento(valor))}.')
print(f'Diminuindo 13& em {moeda.formatacao(valor)}, temos {moeda.formatacao(moeda.reducao(valor))}.')