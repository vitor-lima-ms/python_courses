from lib import dado
from lib import moeda
entrada_usuario = dado.validacao(input('Digite um preco: R$').replace(',', '.').strip())
moeda.resumo(entrada_usuario,
             int(input('Digite um percentual de aumento [%]: ')),
             int(input('Digite um percentual de reducao [%]: ')))