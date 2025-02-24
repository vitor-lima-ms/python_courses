#Desafio 036 - Aula 12 - Mundo 2 (Empréstimo bancário)

valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = float(input('Em quantos anos você pretende pagar a casa? '))

meses = (anos * 12)
prestacao_mensal = (valor_casa / meses)

print('Considerando o valor da casa (R$ {:.2f}) e o tempo de parcelamento ({} anos), o valor da prestação mensal será de: R$ {:.2f}'.format(valor_casa, anos, prestacao_mensal))

if (prestacao_mensal <= (0.3 * salario)):
    print('Empréstimo aprovado! Valor da prestação mensal menor ou igual à 30% do salário.')
else:
    print('Empréstimo negado! Valor da prestação mensal maior que 30% do salário.')


#Desafio 037 - Aula 12 - Mundo 2 (Bases numéricas)




#Desafio 038 - Aula 12 - Mundo 2 (Comparação de valores)

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

if num1 > num2:
    print('O primeiro valor ({}) é maior que o segundo valor ({})'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor ({}) é maior que o primeiro valor ({})'.format(num2, num1))
else:
    print('Os dois números são iguais')


#Desafio 039 - Aula 12 - Mundo 2 (Alistamento militar)

from datetime import date
from time import sleep

idade_ref = 18

nascimento = input('Qual sua data de nascimento (DD/MM/AAAA)? ')

lista_nascimento = nascimento.split('/')
dia_nascimento = int(lista_nascimento[0])
mes_nascimento = int(lista_nascimento[1])
ano_nascimento = int(lista_nascimento[2])

data_atual = str(date.today())
lista_data_atual = data_atual.split('-')
dia_atual = int(lista_data_atual[2])
mes_atual = int(lista_data_atual[1])
ano_atual = int(lista_data_atual[0])

##Condicional pra calcular a idade do sujeito

if mes_nascimento < mes_atual:
    idade_anos = (ano_atual - ano_nascimento)

elif mes_nascimento == mes_atual:
    if dia_nascimento < dia_atual or dia_nascimento == dia_atual:
        idade_anos = (ano_atual - ano_nascimento)
    else:
        idade_anos = (ano_atual - ano_nascimento - 1)        

elif mes_nascimento > mes_atual:
    idade_anos = (ano_atual - ano_nascimento - 1)

print('Você tem {} anos.'.format(idade_anos))
print('Vamos avaliar a sua situação quanto ao alistamento militar.')
print('Carregando...')
sleep(5)

##Condicional para avaliar o alistamento

if idade_anos > idade_ref:
    ano_18 = (ano_nascimento + idade_ref)
    passou = (ano_atual - ano_18)
    
    if passou == 1:
        print('Você já deveria ter se alistado no ano passado!')
    else:
        print('Você já deveria ter se alistado à {} anos!'.format(passou))

elif idade_anos == idade_ref:
    if ((ano_atual - ano_nascimento) == idade_ref) and mes_atual > mes_nascimento: #Para quem completou 18 anos no ano atual
        passou = (mes_atual - mes_nascimento)
        if passou == 1:
            print('Você já deveria ter se alistado no mês passado!')
        else:
            print('Você já deveria ter se alistado à {} meses!'.format(passou)) 
    
    elif (ano_atual - ano_nascimento) == (idade_ref + 1): #Caso a pessoa tenha completado 18 anos no ano anterior mais ainda não tenha feito aniversário no ano atual
        print('Você deveria ter se alistado no ano passado!')
    
    elif mes_atual == mes_nascimento and dia_atual == dia_nascimento:
        print('Você deve se alistar hoje meu garoto!')
    
    elif mes_atual == mes_nascimento and dia_atual > dia_nascimento:
        passou = (dia_atual - dia_nascimento)
        if passou == 1:
            print('Você deveria ter se alistado ontem!')
        else:
            print('Você já deveria ter se alistado à {} dias!'.format(passou))

elif idade_anos < idade_ref:
    ano_18 = (ano_nascimento + idade_ref)
    
    if ano_atual == ano_18:
        if mes_atual < mes_nascimento:
            faltam = (mes_nascimento - mes_atual)
            if faltam == 1:
                print('Você deve se alistar mês que vem')
            else:
                print('Você deve se alistar daqui à {} meses!'.format(faltam))
                
        elif mes_atual == mes_nascimento and dia_atual < dia_nascimento:
            faltam = (dia_nascimento - dia_atual)
            if faltam == 1:
                print('Você deve se alistar amanhã!')
            else:
                print('Você deve se alistar daqui à {} dias!'.format(faltam))
        
    elif ano_atual < ano_18:
        faltam = (ano_18 - ano_atual)    
        if faltam == 1:
            print('Você deve se alistar no ano que vem!')
        else:
            print('Você deve se alistar daqui à {} anos!'.format(faltam))


#Desafio 040 - Aula 12 - Mundo 2 (Média de notas)

from time import sleep

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print('Calculando a média...')
sleep(3)

media = ((nota1 + nota2) / 2)
print('A média obtida pelo aluno foi igual à: {:.2f}'.format(media))

print('Obtendo o resultado final...')
sleep(3)

if media < 5:
    print('Reprovado!!! Nos vemos no ano que vem.')
elif media >= 5 and media < 7:
    print('Em recuperação. Acredita que dá!')
else:
    print('Aprovado, seu nerdola!')


#Desafio 041 - Aula 12 - Mundo 2 (Faixas de idade)

from datetime import date

ano_nascimento = int(input('Qual o ano de nascimento do atleta? '))

ano_atual = int(date.today().year)

idade = (ano_atual - ano_nascimento)

if idade <= 9:
    print('Atleta enquadrado na categoria MIRIM!')
elif idade > 9 and idade <= 14:
    print('Atleta enquadrado na categoria INFANTIL!')
elif idade > 14 and idade <= 19:
    print('Atleta enquadrado na categoria JUNIOR!')
elif idade > 19 and idade <= 20:
    print('Atleta enquadrado na categoria SÊNIOR!')
else:
    print('Atleta enquadrado na categoria MASTER!')


#Desafio 042 - Aula 12 - Mundo 2 (Essas retas formam um triângulo? pt.2)

from time import sleep

##O comprimento de a deve ser menor que b + c e assim sucessivamente

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

pode = ''

print('Analisando...')
sleep(3)

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    pode = True
    print('As retas podem formar um triângulo :)')
    print('Mas qual tipo de triângulo elas podem formar?')
    print('Analisando...')
    sleep(5)
    
else:
    pode = False
    print('As retas não podem formar um triângulo :(')

if pode == True:
    if a == b and a == c and b == c:
        print('O triângulo formado será Equilátero!')
    elif a != b and a != c and b != c:
        print('O triângulo formado será Escaleno!')
    else:
        print('O triângulo formado será Isóceles!')


#Desafio 043 - Aula 12 - Mundo 2 (IMC)

from time import sleep

peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

print('Calculando o IMC...')
sleep(3)

imc = (peso / (altura ** 2))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está obeso!')
else:
    print('Você é um obeso mórbido!')


#Desafio 044 - Aula 12 - Mundo 2 (Preço condicionado à forma de pagamento)

from time import sleep

preco = float(input('Qual o preço do produto (R$)? '))
print('Formas de pagamento:\nÀ vista no dinheiro ou cheque: 10% de desconto;\nÀ vista no cartão: 5% de desconto;\nEm até 2x no cartão: Preço normal;\n3x ou mais no cartão: 20% de juros.')

forma_de_pagamento = input('Qual será a forma de pagamento? ')
forma_de_pagamento_formatada = forma_de_pagamento.lower().strip().replace(' ', '').replace('á', 'a').replace('à', 'a').replace('ã', 'a')

print('Processando...')
sleep(3)

if forma_de_pagamento_formatada == 'avistanodinheiro' or forma_de_pagamento_formatada == 'avistanocheque':
    preco_final = (preco * 0.9)
    print('O preço final é: R$ {:.2f}'.format(preco_final))
elif forma_de_pagamento_formatada == 'avistanocartao':
    preco_final = (preco * 0.95)
    print('O preço final é: R$ {:.2f}'.format(preco_final))
elif forma_de_pagamento_formatada == 'emate2xnocartao':
    preco_final = preco
    print('O preço final é: R$ {:.2f}'.format(preco_final))
elif forma_de_pagamento_formatada == '3xoumaisnocartao':
    preco_final = (preco * 1.2)
    print('O preço final é: R$ {:.2f}'.format(preco_final))
else:
    print('Forma de pagamento não reconhecida. Por favor, tente novamente!')
    forma_de_pagamento = input('Qual será a forma de pagamento? ')
    forma_de_pagamento_formatada = forma_de_pagamento.lower().strip().replace(' ', '').replace('á', 'a').replace('à', 'a').replace('ã', 'a')
    print('Processando...')
    sleep(3)
    while forma_de_pagamento_formatada != 'avistanodinheiro' and forma_de_pagamento_formatada != 'avistanocheque' and forma_de_pagamento_formatada != 'avistanocartao' and forma_de_pagamento_formatada != 'emate2xnocartao' and forma_de_pagamento_formatada != '3xoumaisnocartao':
        print('Forma de pagamento não reconhecida. Por favor, tente novamente!')
        forma_de_pagamento = input('Qual será a forma de pagamento? ')
        forma_de_pagamento_formatada = forma_de_pagamento.lower().strip().replace(' ', '').replace('á', 'a').replace('à', 'a').replace('ã', 'a')
        print('Processando...')
        sleep(3)
        
        if forma_de_pagamento_formatada == 'avistanodinheiro' or forma_de_pagamento_formatada == 'avistanocheque':
            preco_final = (preco * 0.9)
        elif forma_de_pagamento_formatada == 'avistanocartao':
            preco_final = (preco * 0.95)
        elif forma_de_pagamento_formatada == 'emate2xnocartao':
            preco_final = preco
        elif forma_de_pagamento_formatada == '3xoumaisnocartao':
            preco_final = (preco * 1.2)
            
    print('O preço final é: R$ {:.2f}'.format(preco_final))


#Desafio 045 - Aula 12 - Mundo 2 (Jokenpô)

import random
from time import sleep

inicio = input('Olá! Vamos jogar Jokenpô? (S/N) ')
inicio_formatado = inicio.lower().strip()

while inicio_formatado != 's' and inicio_formatado != 'n':
    print('Por favor, escolha S ou N.')
    inicio = input('Vamos jogar Jokenpô? (S/N) ')
    inicio_formatado = inicio.lower().strip()

if inicio_formatado == 's':
    print('Eba! Vamos lá, então!!!')
    sleep(0.5)
    print('Vou escolher entre pedra, papel ou tesoura!')
    sleep(0.5)
    print('Pensando...')
    
    possibilidades = ['pedra', 'papel', 'tesoura']
    escolha_pc = str(random.choice(possibilidades))
    
    sleep(5)
    print('Pronto! Já escolhi. Agora é a sua vez, mas não me mostra ainda!')
    sleep (1.5)
    
    escolha_usuario = input('Pedra, papel ou tesoura? ')
    escolha_usuario_formatado = escolha_usuario.lower().strip()
    while escolha_usuario_formatado != 'pedra' and escolha_usuario_formatado != 'papel' and escolha_usuario_formatado != 'tesoura':
        print('Opção inválida!')
        escolha_usuario = input('Pedra, papel ou tesoura? ')
        escolha_usuario_formatado = escolha_usuario.lower().strip()
    
    sleep(1)
    
    print('Perfeito! Vamos mostrar em...')
    print('3...')
    sleep(1)
    print('2..')
    sleep(1)
    print('1!')
    sleep(1)
    
    print('A minha escolha foi: {}'.format(escolha_pc.capitalize()))
    print('A sua escolha foi: {}'.format(escolha_usuario_formatado.capitalize()))
    sleep(1)
    
    if escolha_usuario_formatado == escolha_pc:
        print('Olha só! Um empate!')
    elif escolha_usuario_formatado == 'pedra' and escolha_pc == 'papel':
        print('Eu ganhei!!!')
    elif escolha_usuario_formatado == 'papel' and escolha_pc == 'tesoura':
        print('Eu ganhei!!!')
    elif escolha_usuario_formatado == 'tesoura' and escolha_pc == 'pedra':
        print('Eu ganhei!!!')
    elif escolha_usuario_formatado == 'pedra' and escolha_pc == 'tesoura':
        print('Você ganhou! Parabéns!!!')
    elif escolha_usuario_formatado == 'papel' and escolha_pc == 'pedra':
        print('Você ganhou! Parabéns!!!')
    elif escolha_usuario_formatado == 'tesoura' and escolha_pc == 'papel':
        print('Você ganhou! Parabéns!!!')
        
    denovo = input('Deseja jogar novamente? (S/N) ')
    denovo_formatado = denovo.lower().strip()
    
    while denovo_formatado != 's' and denovo_formatado != 'n':
        print('Por favor, escolha S ou N.')
        denovo = input('Vamos jogar denovo? (S/N) ')
        denovo_formatado = inicio.lower().strip()
    
    if denovo_formatado == 'n':
        print('Que pena. Até mais!')
    
    while denovo_formatado == 's':
        print('Eba! Vamos lá, então!!!')
        sleep(0.5)
        print('Vou escolher entre pedra, papel ou tesoura!')
        sleep(0.5)
        print('Pensando...')
            
        possibilidades = ['pedra', 'papel', 'tesoura']
        escolha_pc = str(random.choice(possibilidades))
            
        sleep(5)
        print('Pronto! Já escolhi. Agora é a sua vez, mas não me mostra ainda!')
        sleep (1.5)
            
        escolha_usuario = input('Pedra, papel ou tesoura? ')
        escolha_usuario_formatado = escolha_usuario.lower().strip()
        
        while escolha_usuario_formatado != 'pedra' and escolha_usuario_formatado != 'papel' and escolha_usuario_formatado != 'tesoura':
            print('Opção inválida!')
            escolha_usuario = input('Pedra, papel ou tesoura? ')
            escolha_usuario_formatado = escolha_usuario.lower().strip()
        
        sleep(1)
            
        print('Perfeito! Vamos mostrar em...')
        print('3...')
        sleep(1)
        print('2..')
        sleep(1)
        print('1!')
        sleep(1)
            
        print('A minha escolha foi: {}'.format(escolha_pc.capitalize()))
        print('A sua escolha foi: {}'.format(escolha_usuario_formatado.capitalize()))
        sleep(1)
            
        if escolha_usuario_formatado == escolha_pc:
            print('Olha só! Um empate!')
        elif escolha_usuario_formatado == 'pedra' and escolha_pc == 'papel':
            print('Eu ganhei!!!')
        elif escolha_usuario_formatado == 'papel' and escolha_pc == 'tesoura':
            print('Eu ganhei!!!')
        elif escolha_usuario_formatado == 'tesoura' and escolha_pc == 'pedra':
            print('Eu ganhei!!!')
        elif escolha_usuario_formatado == 'pedra' and escolha_pc == 'tesoura':
            print('Você ganhou! Parabéns!!!')
        elif escolha_usuario_formatado == 'papel' and escolha_pc == 'pedra':
            print('Você ganhou! Parabéns!!!')
        elif escolha_usuario_formatado == 'tesoura' and escolha_pc == 'papel':
            print('Você ganhou! Parabéns!!!')
                
        denovo = input('Deseja jogar novamente? (S/N) ')
        denovo_formatado = denovo.lower().strip()
            
        while denovo_formatado != 's' and denovo_formatado != 'n':
            print('Por favor, escolha S ou N.')
            denovo = input('Vamos jogar denovo? (S/N)')
            denovo_formatado = inicio.lower().strip()


elif inicio_formatado == 'n':
    print('Que pena. Até mais!')
    
    
#Desafio 046 - Aula 13 - Mundo 2 (Contagem regressiva)

from time import sleep
from datetime import date

for i in range(10, 0, -1):
    if i >=3:
        print('{}...'.format(i))
        sleep(1)
    elif i == 2:
        print('{}..'.format(i))
        sleep(1)
    elif i == 1:
        print('{}!'.format(i))
        sleep(1)
print('Feliz {}!'.format((date.today().year) + 1))


#Desafio 047 - Aula 13 - Mundo 2 (Números pares em um determinado intervalo)

inicio = 1
fim = 50

print('Lista de números pares entre {} e {}:'.format(inicio, fim))
for i in range(inicio, (fim + 1)):
    if i % 2 == 0:
        print(i)


#Desafio 048 - Aula 13 - Mundo 2 (Calculadora de números ímpares dentro de um determinado intervalo)

inicio = 1
fim = 500

soma = 0
quantos = 0

for i in range(inicio, (fim + 1)):
    if i % 2 != 0 and i % 3 == 0:
        soma = soma + i
        quantos = quantos + 1
        
print('O resultado da soma dos {} números ímpares entre {} e {} é {}'.format(quantos, inicio, fim, soma))


#Desafio 049 - Aula 13 - Mundo 2 (Tabuada)

numero = int(input('Digite o número inteiro para o qual você gostaria que a tabuada fosse criada: '))

print('Tabuada do número {}'.format(numero))

for i in range(0, 11):
    resultado = (numero * i)
    print('{} x {} = {}'.format(i, numero, resultado))


#Desafio 050 - Aula 13 - Mundo 2 (Soma de pares)

soma_par = 0
cont_par = 0

for i in range(1, 7):
    num = int(input('Digite o {}° número inteiro: '.format(i)))
    if num % 2 == 0:
        soma_par = soma_par + num
        cont_par = cont_par + 1

if cont_par == 0:
    print('Nenhum número par foi informado!')
elif cont_par == 1:
    print('Apenas um número par ({}) foi informado.'.format(soma_par))
else:
    print('A soma dos {} números pares presentes entre os 6 números informados é: {}.'.format(cont_par, soma_par))

#Desafio 051 - Aula 13 - Mundo 2 (P.A)

primeiro_termo = int(input('Informe um número inteiro para ser o primeiro termo da P.A: '))
razao = int(input('Informe a razão da P.A: '))

print('P.A - Primeiro termo = {} - Razão = {}:'.format(primeiro_termo, razao))
for i in range(1, 11):
     termo = (primeiro_termo + ((i - 1) * razao))
     print('O {}° termo é: {}'.format(i, termo))


#Desafio 052 - Aula 13 - Mundo 2 (Números primos)

num = int(input('Digite um número inteiro para verificar se ele é primo: '))

aux = 0

for i in range(1, num):
    if i == 1:
        continue
    elif num % i == 0:
        aux = aux + 1

if aux >= 1:
    print('O número {} não é primo!'.format(num))
else:
    print('O número {} é primo!'.format(num))
    
    
#Desafio 053 - Aula 13 - Mundo 2 (Palíndromo)

frase = input('Escreva uma frase para verificar se ela é um palíndromo: ')
frase_formatada = frase.lower().strip().replace(' ', '')

aux = ''

for i in range((len(frase_formatada) - 1), -1, -1):
    aux = aux + frase_formatada[i]
        
if frase_formatada == aux:
    print('A frase {} é um palíndromo'.format(frase.strip()))


#Desafio 054 - Aula 13 - Mundo 2 (Maioridade)

from datetime import date

maiores = 0
menores = 0

for i in range(1, 8):
    ano = int(input('Qual o ano de nascimento da {}° pessoa? '.format(i)))
    idade = ((date.today().year) - ano)
    if idade >= 21:
        maiores = maiores + 1
    else:
        menores = menores + 1
        
print('Das 7 pessoas, {} são maiores de idade e {} são menores de idade!'.format(maiores, menores))


#Desafio 055 - Aula 13 - Mundo 2 (Comparação de pesos)

maior = 0.0
menor = 0.0

pessoa_maior = 0
pessoa_menor = 0

for i in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa (Kg): '.format(i)))
    if peso > maior:
        maior = peso
        pessoa_maior = i
    if menor == 0.0:
        menor = peso
        pessoa_menor = i
    elif peso < menor:
        menor = peso
        pessoa_menor = i

print('A {}° pessoa, que pesa {:.2f} Kg, tem o maior peso!'.format(pessoa_maior, maior))
print('A {}° pessoa, que pesa {:.2f} Kg, tem o menor peso!'.format(pessoa_menor, menor))


#Desafio 056 - Aula 13 - Mundo 2 (Estatísticas de um grupo de pessoas)

soma_idades = 0
idade_homem_velho = 0
nome_homem_velho = ''
mulheres_menos_20 = 0

for i in range(1, 5):
    print('Olá {}° pessoa!'.format(i))
    nome = input('Qual o seu nome? ')
    idade = int(input('Qual a sua idade? '))
    
    sexo = input('Qual o seu sexo biológico (H/M)? ')
    sexo_formatado = sexo.lower().strip()
    
    soma_idades = soma_idades + idade
    
    if sexo_formatado == 'h' and idade > idade_homem_velho:
        idade_homem_velho = idade
        nome_homem_velho = nome
    
    if sexo_formatado == 'm' and idade < 20:
        mulheres_menos_20 = mulheres_menos_20 + 1

media = soma_idades / i

print('Características do grupo!')
print('A média de idade é: {} anos;'.format(media))
print('O homem mais velho se chama: {};'.format(nome_homem_velho))
print('Dentre as mulheres, {} tem menos de 20 anos.'.format(mulheres_menos_20))


#Desafio 057 - Aula 14 - Mundo 2 (Valor correto)

sexo = input('Qual o seu sexo biológico [M/F]? ')

while sexo != 'M' and sexo != 'F':
    print('Valor inválido! Por favor, escolha entre M e F.')
    sexo = input('Qual o seu sexo biológico [M/F]? ')

denovo = input('Deseja fazer uma nova consulta [S/N]? ')

while denovo != 'S' and denovo != 'N':
    print('Valor inválido! Por favor, escolha entre S e N.')
    denovo = input('Deseja fazer uma nova consulta [S/N]? ')
    
while denovo == 'S':
    sexo = input('Qual o seu sexo biológico [M/F]? ')

    while sexo != 'M' and sexo != 'F':
        print('Valor inválido! Por favor, escolha entre M e F.')
        sexo = input('Qual o seu sexo biológico [M/F]? ')
            
    denovo = input('Deseja fazer uma nova consulta [S/N]? ')
        
print('Fim!')


#Desafio 058 - Aula 14 - Mundo 2 (Desafio 28 melhorado)

from time import sleep
import random

print('Jogo da adivinhação!')
sleep(1.5)

print('Olá! Vou pensar em um número inteiro e você tenta acertar, ok?')
sleep(1)

print('Pensando...')
random_num = random.randint(1, 10)
sleep(3)

print('Pronto! Agora, tente acertar xD')

num = int(input('Qual o seu palplite? '))

print('Conferindo...')
sleep(2)

tentativa = 1

while num != random_num:
    print('Ops... Você não acertou =(')
    sleep(1)
    print('Tente novamente!')
    sleep(0.5)
    num = int(input('Qual o seu palplite? '))
    
    tentativa = tentativa + 1

print('Parabéns! Você acertou o número ({}) que eu pensei na {}ª tentativa!'.format(random_num, tentativa))

denovo = input('Quer jogar denovo [S/N]? ')

while denovo != 'S' and denovo != 'N':
    print('Opção inválida! Escolha entre S e N.')
    denovo = input('Quer jogar denovo [S/N]? ')

while denovo == 'S':
    print('Então, vamos lá')
    sleep(0.5)
    
    print('Pensando em outro número...')
    random_num = random.randint(1, 10)
    sleep(3)
    
    print('Pronto! Agora, tente acertar xD')

    num = int(input('Qual o seu palplite? '))

    print('Conferindo...')
    sleep(2)

    tentativa = 1
    
    while num != random_num:
        print('Ops... Você não acertou =(')
        sleep(1)
        print('Tente novamente!')
        sleep(0.5)
        num = int(input('Qual o seu palplite? '))
        
        tentativa = tentativa + 1

    print('Parabéns! Você acertou o número ({}) que eu pensei na {}ª tentativa!'.format(random_num, tentativa))

    denovo = input('Quer jogar denovo [S/N]? ')

    while denovo != 'S' and denovo != 'N':
        print('Opção inválida! Escolha entre S e N.')
        denovo = input('Quer jogar denovo [S/N]? ')
        
print('Que pena! Foi um prazer jogar com você!')


#Desafio 059 - Aula 14 - Mundo 2 (Calculadora)

from time import sleep

sleep(0.5)

print('Calculadora simples.')
sleep(0.5)

num1 = float(input('Digite o primeiro número: '))
sleep(0.5)
num2 = float(input('Digite o segundo número: '))
sleep(0.5)

print('Menu de opções:')
print('[1] Soma;')
print('[2] Multiplicação;')
print('[3] Maior;')
print('[4] Novos números;')
print('[5] Sair do programa.')
sleep(1)

opcao = int(input('Escolha uma opção: '))

while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
    print('Opção inválida!')
    opcao = int(input('Escolha uma opção: '))

if opcao == 5:
    sleep(0.5)
    print('Encerrando...')
    sleep(0.5)
    
elif opcao == 1:
    sleep(0.5)
    print('Somando {} e {}...'. format(num1, num2))
    resultado = num1 + num2
    sleep(1)
    print('O resultado da soma é: {:.2f}.'.format(resultado))

elif opcao == 2:
    sleep(0.5)
    print('Multiplicando {} e {}...'. format(num1, num2))
    resultado = num1 * num2
    sleep(1)
    print('O resultado da multiplicação é: {:.2f}.'.format(resultado))

elif opcao == 3:
    sleep(0.5)
    print('Processando qual número é maior entre {} e {}...'. format(num1, num2))
    if num1 > num2:
        resultado = num1
        print('O maior número é: {:.2f}.'.format(resultado))
    elif num1 == num2:
        print('Os dois números são iguais!')
    else:
        resultado = num2
        print('O maior número é: {:.2f}.'.format(resultado))
    sleep(1)
    
while opcao == 4:
    num1 = float(input('Digite o novo primeiro número: '))
    sleep(0.5)
    num2 = float(input('Digite o novo segundo número: '))
    sleep(0.5)

    print('Menu de opções:')
    print('[1] Soma;')
    print('[2] Multiplicação;')
    print('[3] Maior;')
    print('[4] Novos números;')
    print('[5] Sair do programa.')
    sleep(1)

    opcao = int(input('Escolha uma opção: '))

    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
        print('Opção inválida!')
        opcao = int(input('Escolha uma opção: '))

    if opcao == 5:
        sleep(0.5)
        print('Encerrando...')
        sleep(0.5)
        break
        
    elif opcao == 1:
        sleep(0.5)
        print('Somando {} e {}...'. format(num1, num2))
        resultado = num1 + num2
        sleep(1)
        print('O resultado da soma é: {:.2f}.'.format(resultado))

    elif opcao == 2:
        sleep(0.5)
        print('Multiplicando {} e {}...'. format(num1, num2))
        resultado = num1 * num2
        sleep(1)
        print('O resultado da multiplicação é: {:.2f}.'.format(resultado))

    elif opcao == 3:
        sleep(0.5)
        print('Processando qual número é maior entre {} e {}...'. format(num1, num2))
        if num1 > num2:
            resultado = num1
            print('O maior número é: {:.2f}.'.format(resultado))
        elif num1 == num2:
            print('Os dois números são iguais!')
        else:
            resultado = num2
            print('O maior número é: {:.2f}.'.format(resultado))
        sleep(1)

if opcao == 5:
    denovo = 'N'
    print('Até mais!')
else:
    denovo = input('Deseja realizar uma nova operação [S/N]? ')

while denovo != 'S' and denovo != 'N':
    print('Opção inválida!')
    denovo = input('Escolha uma opção [S/N]: ')
    
while denovo == 'S':
    sleep(0.5)

    num1 = float(input('Digite o primeiro número: '))
    sleep(0.5)
    num2 = float(input('Digite o segundo número: '))
    sleep(0.5)

    print('Menu de opções:')
    print('[1] Soma;')
    print('[2] Multiplicação;')
    print('[3] Maior;')
    print('[4] Novos números;')
    print('[5] Sair do programa.')
    sleep(1)

    opcao = int(input('Escolha uma opção: '))

    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
        print('Opção inválida!')
        opcao = int(input('Escolha uma opção: '))

    if opcao == 5:
        sleep(0.5)
        print('Encerrando...')
        denovo = 'N'
        sleep(0.5)
        break
        
    elif opcao == 1:
        sleep(0.5)
        print('Somando {} e {}...'. format(num1, num2))
        resultado = num1 + num2
        sleep(1)
        print('O resultado da soma é: {:.2f}.'.format(resultado))

    elif opcao == 2:
        sleep(0.5)
        print('Multiplicando {} e {}...'. format(num1, num2))
        resultado = num1 * num2
        sleep(1)
        print('O resultado da multiplicação é: {:.2f}.'.format(resultado))

    elif opcao == 3:
        sleep(0.5)
        print('Processando qual número é maior entre {} e {}...'. format(num1, num2))
        if num1 > num2:
            resultado = num1
            print('O maior número é: {:.2f}.'.format(resultado))
        elif num1 == num2:
            print('Os dois números são iguais!')
        else:
            resultado = num2
            print('O maior número é: {:.2f}.'.format(resultado))
        sleep(1)

    while opcao == 4:
        num1 = float(input('Digite o novo primeiro número: '))
        sleep(0.5)
        num2 = float(input('Digite o novo segundo número: '))
        sleep(0.5)

        print('Menu de opções:')
        print('[1] Soma;')
        print('[2] Multiplicação;')
        print('[3] Maior;')
        print('[4] Novos números;')
        print('[5] Sair do programa.')
        sleep(1)

        opcao = int(input('Escolha uma opção: '))

        while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
            print('Opção inválida!')
            opcao = int(input('Escolha uma opção: '))

        if opcao == 5:
            sleep(0.5)
            print('Encerrando...')
            denovo = 'N'
            sleep(0.5)
            break
            
        elif opcao == 1:
            sleep(0.5)
            print('Somando {} e {}...'. format(num1, num2))
            resultado = num1 + num2
            sleep(1)
            print('O resultado da soma é: {:.2f}.'.format(resultado))

        elif opcao == 2:
            sleep(0.5)
            print('Multiplicando {} e {}...'. format(num1, num2))
            resultado = num1 * num2
            sleep(1)
            print('O resultado da multiplicação é: {:.2f}.'.format(resultado))

        elif opcao == 3:
            sleep(0.5)
            print('Processando qual número é maior entre {} e {}...'. format(num1, num2))
            if num1 > num2:
                resultado = num1
                print('O maior número é: {:.2f}.'.format(resultado))
            elif num1 == num2:
                print('Os dois números são iguais!')
            else:
                resultado = num2
                print('O maior número é: {:.2f}.'.format(resultado))
            sleep(1)

    if opcao == 5:
        denovo = 'N'
        print('Até mais!')
    else:
        denovo = input('Deseja realizar uma nova operação [S/N]? ')
    
    while denovo != 'S' and denovo != 'N':
        print('Opção inválida!')
        denovo = input('Escolha uma opção [S/N]: ')
    

#Desafio 060 - Aula 14 - Mundo 2 (Fatorial)

##For

num = int(input('Digite um número inteiro para descobrir o seu fatorial: '))

aux = 1

for i in range (2, num): #
    aux = aux * i
    
fatorial = num * aux

print('O fatorial de {} é {}.'.format(num, fatorial))

##While

num = int(input('Digite um número inteiro para descobrir o seu fatorial: '))

cont = 0
aux = 1

while cont < (num - 1):
    cont = cont + 1
    aux = aux * cont
    
fatorial = num * aux

print('O fatorial de {} é {}.'.format(num, fatorial))


#Desafio 061 - Aula 14 - Mundo 2 (P.A com while)

primeiro_termo = int(input('Informe um número inteiro para ser o primeiro termo da P.A: '))
razao = int(input('Informe a razão da P.A: '))

print('P.A - Primeiro termo = {} - Razão = {}:'.format(primeiro_termo, razao))

#termo_n = (primeiro_termo + ((n - 1) * razao))

n = 1

while n <= 10:
    termo_n = (primeiro_termo + ((n - 1) * razao))
    print('{}° termo = {}'.format(n, termo_n))
    n = n + 1


#Desafio 062 - Aula 14 - Mundo 2 (Melhoria do desafio 061)

primeiro_termo = int(input('Informe um número inteiro para ser o primeiro termo da P.A: '))
razao = int(input('Informe a razão da P.A: '))

print('P.A - Primeiro termo = {} - Razão = {}:'.format(primeiro_termo, razao))

#termo_n = (primeiro_termo + ((n - 1) * razao))

n = 1
ultimo_termo = 0

while n <= 10:
    termo_n = (primeiro_termo + ((n - 1) * razao))
    print('{}° termo = {}'.format(n, termo_n))
    n = n + 1
    if n == 11:
        ultimo_termo = termo_n
    
continuar = input('Deseja mostrar mais termos [S/N]? ')

while continuar != 'S' and continuar != 'N':
    print('Opção inválida!')
    continuar = input('Deseja mostrar mais termos [S/N]? ')

if continuar == 'S':
    quantos = int(input('Quantos termos a mais você deseja mostrar após o décimo? '))

while continuar == 'S' and quantos > 0:
    for i in range(1, (quantos + 1)):
        termo_i = ultimo_termo +  razao
        print('{}° termo após o último: {}'.format(i, termo_i))
        ultimo_termo = termo_i
    
    continuar = input('Deseja mostrar mais termos [S/N]? ')

    while continuar != 'S' and continuar != 'N':
        print('Opção inválida!')
        continuar = input('Deseja mostrar mais termos [S/N]? ')

    if continuar == 'S':
        quantos = int(input('Quantos termos a mais você deseja mostrar após o último? '))

print('Tudo bem. Até logo!')


#Desafio 063 - Aula 14 - Mundo 2 (Sequência de Fibonacci)

from time import sleep

print('Sequência de Fibonacci')
sleep(1)

num = int(input('Digite um número inteiro: '))
sleep(0.5)
print('Calculando...')
sleep(2)

lista_fibo = []

for i in range(1, (num + 1)):
    if i == 1:
        lista_fibo.append(0)
    elif i == 2:
        lista_fibo.append(1)
    else:
        termo_n = lista_fibo[(i - 3)] + lista_fibo[(i - 2)]
        lista_fibo.append(termo_n)

if num == 1:
    print('O primeiro termo na sequência de Fibonacci é: {}'.format(lista_fibo[0]))
else:
    print('A sequência de Fibonacci até o {}° termo é:'.format(num))
    print(lista_fibo)


#Desafio 064 - Aula 14 - Mundo 2 (Valor de interrupção)

n = 0
cont = 0
soma = 0

while True:
    n = int(input('Digite um número inteiro positivo: '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n

print('A soma dos {} números digitados é {}.'.format(cont, soma))
        

#Desafio 065 - Aula 14 - Mundo 2

from time import sleep

print('Bem vindo à calculadora estatística básica!\n')
sleep(1)
print('''Aqui, você pode digitar quantos números quiser pois, ao final da
execução, te mostraremos a média dos valores, qual foi o maior valor
digitado, bem como o menor valor!\n''')

comecar = input('Vamos começar [S]? ')

while comecar != 'S':
    print('Opção inválida!')
    comecar = input('Vamos começar [S]? ')

continuar = comecar

cont = 0
soma = 0
maior = 0
menor = 0

while continuar == 'S':
    num = int(input('Digite um número inteiro: '))
    cont = cont + 1
    soma = soma + num
    if num > maior:
        maior = num
    if cont == 1:
        menor = num
    if num < menor:
        menor = num
    continuar = input('Deseja continuar digitando [S/N]? ')
    while continuar != 'S' and continuar != 'N':
        print('Opção inválida!')
        continuar = input('Deseja continuar digitando [S/N]? ')

print('Calculando as estatísticas...')
media = soma / cont
sleep(2)

print('Soma = {};'.format(soma))
print('Média = {};'.format(media))
print('Maior = {};'.format(maior))
print('Menor = {}.'.format(menor))


#Desafio 066 - Aula 15 - Mundo 2 (Condição de parada)

cont = 0
soma = 0

while True:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n

if cont == 1:
    print('Você digitou apenas um número')
else:
    print(f'A soma dos {cont} números que você digitou é {soma}!')


#Desafio 067 - Aula 15 - Mundo 2 (Tabuada)

from time import sleep

while True:
    num = int(input('Digite um número inteiro positivo para ver a sua tabuada: '))
    sleep(1)
    print('\nCalculando...')
    sleep(2)
    print(f'\nTabuada do número {num}.')
    for i in range(1, 11):
        resultado = num * i
        print(f'{num} x {i} = {resultado}')
    print('\nDeseja ver a tabuada de outro número?\n')
    continuar = input('[1] para Sim e [-1] para Não: ')
    while continuar != '1' and continuar != '-1':
        print('Opção inválida!')
        continuar = input('[1] para Sim e [-1] para Não: ')
    if continuar == '-1':
        break
print('\nObrigado por utilizar meu serviço!')


#Desafio 068 - Aula 15 - Mundo 2 (Par ou ímpar)

from time import sleep
import random

print('Par ou Ímpar!')
sleep(1)

cont_vitórias = 0

while True:
    print('Vou escolher um número entre 0 e 10! Só um momento...')
    random_num = random.randint(0, 10)
    sleep(2)
    print('Pronto! Agora é a sua vez.')
    sleep(0.5)
    print('Escolha um número inteiro entre 0 e 10. Prometo que não estou vendo!')
    user_num = int(input('Digite seu número aqui: '))
    soma = random_num + user_num
    user_poui = input('Agora, escolha Par ou Ímpar: ')
    while user_poui != 'Par' and user_poui != 'Ímpar':
        print('Opção inválida!')
        user_poui = input('Escolha Par ou Ímpar: ')
    print(f'Eu joguei {random_num} e você jogou {user_num}!')
    if soma % 2 == 0 and user_poui == 'Par':
        cont_vitórias += 1
        print(f'Parabéns! Você venceu, {soma} é Par! Vamos jogar denovo.')
    elif soma % 2 == 0 and user_poui == 'Ímpar':
        print(f'Putz... Você perdeu, {soma} é Par! Seu total de vitórias foi de {cont_vitórias}.')
        break
    elif soma % 2 != 0 and user_poui == 'Ímpar':
        cont_vitórias += 1
        print(f'Parabéns! Você venceu, {soma} é Ímpar! Vamos jogar denovo.')
    elif soma % 2 != 0 and user_poui == 'Par':
        print(f'Putz... Você perdeu, {soma} é Ímpar! Seu total de vitórias foi de {cont_vitórias}.')
        break


#Desafio 069 - Aula 15 - Mundo 2 (Cadastro de pessoas)

cont = 1
cont_18p = 0
cont_h = 0
cont_m_20m = 0
continuar = ''
    
while True:
    nome = input(f'\nNome do {cont}° cadastrado: ')
    idade = int(input(f'\nIdade do {cont}° cadastrado: '))
    sexo = input(f'\nSexo biológico do {cont}° cadastrado [M/F]: ')
    while sexo != 'M' and sexo != 'F':
        print('Opção inválida!')
        sexo = input(f'Sexo biológico do {cont}° cadastrado [M/F]: ')
    if idade > 18:
        cont_18p += 1
    if sexo == 'M':
        cont_h += 1
    if sexo == 'F' and idade < 20:
        cont_m_20m += 1
    cont += 1
    print('\nDeseja cadastrar mais alguma pessoa?')
    continuar = input('[S/N]: ')
    while continuar != 'S' and continuar != 'N':
        print('Opção inválida!')
        print('Deseja cadastrar mais alguma pessoa?')
        continuar = input('[S/N]: ')
    if continuar == 'N':
        break
    
print('Resumo:\n')
print(f'A quantidade cadastrada de pessoas com idade maior que 18 é: {cont_18p};')
print(f'\nA quantidade de homens cadastrados é: {cont_h};')
print(f'\nA quantidade cadastrada de mulheres com idade inferior à 20 anos e: {cont_m_20m}.')


#Desafio 070 - Aula 15 - Mundo 2 (Cadastro de compras)

total = 0
cont_1000p = 0
cont = 0
preco_prod_barato = 0
nome_prod_barato = ''

while True:
    nome = input('\nDigite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    total += preco
    if preco > 1000:
        cont_1000p += 1
    if cont == 0:
        preco_prod_barato = preco
        nome_prod_barato = nome
    if preco < preco_prod_barato:
        preco_prod_barato = preco
        nome_prod_barato = nome
    cont += 1
    print('\nDeseja adicionar mais algum produto?')
    continuar = input('[S/N]: ')
    while continuar != 'S' and continuar != 'N':
        print('\nOpção inválida!')
        print('Deseja adicionar mais algum produto?')
        continuar = input('[S/N]: ')
    if continuar == 'N':
        break

print('\nResumo:\n')
print(f'O total gasto nas compras foi de: R${total:.2f};')
print(f'Quantidade de produtos que custam mais que R$1000: {cont_1000p};')
print(f'Nome do produto mais barato: {nome_prod_barato} (R${preco_prod_barato:.2f}).')


#Desafio 071 - Aula 15 - Mundo 2 (Caixa eletrônico)

from time import sleep

while True:
    qtd_cedulas_50 = 0
    qtd_cedulas_20 = 0
    qtd_cedulas_10 = 0
    qtd_cedulas_1 = 0
    print('CAIXA ELETRÔNICO 24hs')
    print('\nIniciando...')
    sleep(2)
    valor = int(input('\nQual o valor a ser sacado? R$'))
    print('Calculando...')
    sleep(0)
    limite = 0
    if valor >= 50:
        qtd_cedulas_50 = valor // 50
        limite += (qtd_cedulas_50 * 50)
        falta = valor - limite
        if falta != 0:
            qtd_cedulas_20 = falta // 20
            limite += (qtd_cedulas_20 * 20)
            falta = valor - limite
            if falta != 0:
                qtd_cedulas_10 = falta // 10
                limite += (qtd_cedulas_10 * 10)
                falta = valor - limite
                if falta != 0:
                    qtd_cedulas_1 = falta
                    limite += qtd_cedulas_1
        elif falta >= 10 and falta < 20:
            qtd_cedulas_10 = falta // 10
            limite += (qtd_cedulas_10 * 10)
            falta = valor - limite
        else:
            qtd_cedulas_1 = falta
            limite += qtd_cedulas_1            
    elif valor >= 20 and valor < 50:
        qtd_cedulas_20 = valor // 20
        limite += (qtd_cedulas_20 * 20)
        falta = valor - limite
        if falta != 0:
            qtd_cedulas_10 = falta // 10
            limite += (qtd_cedulas_10 * 10)
            falta = valor - limite
            if falta != 0:
                qtd_cedulas_1 = falta
                limite += qtd_cedulas_1
    elif valor >= 10 and valor < 20:
        qtd_cedulas_10 = valor // 10
        limite += (qtd_cedulas_10 * 10)
        falta = valor - limite
        if falta != 0:
            qtd_cedulas_1 = falta
            limite += qtd_cedulas_1
    elif valor < 10:
        qtd_cedulas_1 = valor
    if qtd_cedulas_50 > 0:
        print(f'Você receberá {qtd_cedulas_50} cédula(s) de R$50')
    if qtd_cedulas_20 > 0:
        print(f'Você receberá {qtd_cedulas_20} cédula(s) de R$20')
    if qtd_cedulas_10 > 0:
        print(f'Você receberá {qtd_cedulas_10} cédula(s) de R$10')
    if qtd_cedulas_1 > 0:
        print(f'Você receberá {qtd_cedulas_1} cédula(s) de R$1')
    total = (qtd_cedulas_50 * 50) + (qtd_cedulas_20 * 20) + (qtd_cedulas_10 * 10) + (qtd_cedulas_1)
    print(f'Total: R${total}')
    print('\nDeseja realizar mais um saque?')
    continuar = input('[S/N]: ')
    while continuar != 'S' and continuar != 'N':
        print('\nOpção inválida!')
        print('Deseja realizar mais um saque?')
        continuar = input('[S/N]: ')
    if continuar == 'N':
        break
