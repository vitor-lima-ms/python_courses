tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'Sao Paulo', 'Cotinthians', 'Bahia',
          'Cruzeiro', 'Vasco da Gama', 'Vitoria', 'Atletico Mineiro', 'Fluminense', 'Gremio', 'Juventude', 'Bragantino',
          'Chapecoense', 'Criciuma', 'Altetico Goianiense', 'Cuiaba')
print(f'Os cinco primeiros colocados do Brasileirao de 2024 sao: {tabela[0:4]}')
print(f'Os ultimos quatro colocados da tabela sao: {tabela[-4:-1]}')
print(f'A organizacao dos times em ordem alfabetica e: {sorted(tabela)}')
print('A Chapecoense terminou em {} lugarw'.format((tabela.index('Chapecoense') + 1)))