nome = input('Qual é o seu nome? ')
print('Olá, {}! Prazer em te conhecer!'.format(nome))

nome = input('Qual é o seu nome? ')
print('Olá, {:20}! Prazer em te conhecer!'.format(nome)) #Força que o nome seja exibido com 20 caracteres

nome = input('Qual é o seu nome? ')
print('Olá, {:>20}! Prazer em te conhecer!'.format(nome)) #Alinhamento à direita. '<' alinha à esquerda, '^' alinha ao centro, '=^' centraliza com '=' ao redor

print('Primeira linha\nSegunda linha') #Quebra de linha

#f Strings

nome = 'Vitor'
idade = 24

print(f'Oi, meu nome é {nome} e tenho {idade} anos.')

nome = 'Vitor'
idade = 24
salario = 1000.00

print(f'Oi, meu nome é {nome}, tenho {idade} anos e ganho R${salario} por mês.')
print(f'Oi, meu nome é {nome}, tenho {idade} anos e ganho R${salario:.2f} por mês.')