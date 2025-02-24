#Desafio 005 - Aula 07 - Mundo 1 (Antecessor e sucessor)

num = float(input('Digite um número: '))

antecessor = num - 1
sucessor = num + 1

print('O antecessor de {} é {}, e o sucessor de {} é {}'.format(num, antecessor, num, sucessor))


#Desafio 006 - Aula 07 - Mundo 1 (Dobro, triplo e raiz quadrada de um número qualquer)

num = float(input('Digite um número: '))

dobro = num * 2
triplo = num *3
raiz_2 = num ** (1/2)

print('O dobro de {} é {},\nO triplo de {} é {} e\nA raiz quadrada de {} é {:.2f}'.format(num, dobro, num, triplo, num, raiz_2))


#Desafio 007 - Aula 07 - Mundo 1 (Média entre dois valores)

nota1 = float(input('Qual a primeira nota do aluno? '))
nota2 = float(input('Qual a segunda nota do aluno? '))

media = ((nota1 + nota2) / 2)

print('A média das notas do aluno é: {:.1f}'.format(media))


#Desafio 008 - Aula 07 - Mundo 1 (Conversão de metros para cm e mm)

metros = float(input('Qual o valor em metros? '))

mm = (metros * 1000)
cm = (metros * 100)

print('{} metros equivalem à {} milímetros e {} centímetros'.format(metros, mm, cm))


#Desafio 009 - Aula 07 - Mundo 1 (Tabuada)

num = float(input('Qual número você deseja exibir a tabuada? '))

um = (num * 1)
dois = (num * 2)
tres = (num * 3)
quatro = (num * 4)
cinco = (num * 5)
seis = (num * 6)
sete = (num * 7)
oito = (num * 8)
nove = (num * 9)
dez = (num * 10)

print('A tabuada de {} é:\n1x{} = {}\n2x{} = {}\n3x{} = {}\n4x{} = {}\n5x{} = {}\n6x{} = {}\n7x{} = {}\n8x{} = {}\n9x{} = {}\n10x{} = {}'.format(num,
                                                                   num, um,
                                                                   num, dois,
                                                                   num, tres,
                                                                   num, quatro,
                                                                   num, cinco,
                                                                   num, seis,
                                                                   num, sete,
                                                                   num, oito,
                                                                   num, nove,
                                                                   num, dez))


#Desafio 010 - Aula 07 - Mundo 1 (Conversor de moeda)

real = float(input('Quantos reais você tem? '))

dolar = (real/3.27)

print('Essa quantia em reais equivale à {:.2f} dólares'.format(dolar))


#Desafio 011 - Aula 07 - Mundo 1 (Cálculo de área e quantidade de tinta)

largura = float(input('Qual a largura da parede, em metros? '))
altura = float(input('Qual a altura da parede, em metros? '))

area = (largura * altura)

tinta = (area / 2)

print('A área da parede é {} m² e a quantidade de tinta necessária para pintá-la é {} L'.format(area, tinta))


#Desafio 012 - Aula 07 - Mundo 1 (Desconto em produto)

preco = float(input('Qual o valor do produto, em reais? '))

preco_desconto = (preco * 0.95)

print('O preço com 5% de desconto é {:.2f} reais'.format(preco_desconto))


#Desafio 013 - Aula 07 - Mundo 1 (Aumento salarial)

salario = float(input('Qual seu salário atual? '))

aumento = (salario * 1.15)

print('Seu novo salário, com 15% de aumento, é R$ {:.2f}'.format(aumento))


#Desafio 014 - Mundo 1 (Conversor de temperaturas)

celsius = float(input('Digite a temperatura em graus Celsius: '))

fahr = (celsius * (9/5) + 32)

print('Essa temperatura em Celsius equivale à {:.1f} graus Fahrenheit'.format(fahr))


#Desafio 015 - Mundo 1 (Aluguel de carro)

dias = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos Km foram rodados? '))

custo = ((60 * dias) + (0.15 * km))

print('Considerando que o carro ficou alugado por {} dias e rodou {} Km, o preço a pagar é R$ {}'.format(dias, km, custo))


#Desafio 016 - Aula 08 - Mundo 1 (Parte inteira de números)

import math

num = float(input('Digite um número: '))

int_num = math.trunc(num)

print('O número {} possui a parte inteira {}'.format(num, int_num))


#Desafio 017 - Aula 08 - Mundo 1 (Cateto op e adj)

import math

c_op = float(input('Qual o comprimento do cateto oposto? '))
c_adj = float(input('Qual o comprimento do cateto adjacente? '))

hipotenusa = math.hypot(c_op, c_adj)

print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))


#Desafio 018 - Aula 08 - Mundo 1 (Seno, cosseno e tangente de um ângulo qualquer)

import math

ang = float(input('Digite o valor de um ângulo qualquer, em graus: '))

ang_rad = math.radians(ang)

seno = math.sin(ang_rad)
cosseno = math.cos(ang_rad)
tg = math.tan(ang_rad)

print('O seno, cosseno e tangente do ângulo {} graus são, respectivamente, {:.3f}, {:.3f} e {:.3f}'.format(ang, seno, cosseno, tg))


#Desafio 019 - Aula 08 - Mundo 1 (Valor aleatório)

import random

aluno1 = input('Qual o nome do aluno 1? ')
aluno2 = input('Qual o nome do aluno 2? ')
aluno3 = input('Qual o nome do aluno 3? ')
aluno4 = input('Qual o nome do aluno 4? ')

lista = [aluno1, aluno2, aluno3, aluno4]

num_sorteado = random.randint(0, 3)
aluno_sorteado = lista[num_sorteado]

print('{} foi sorteado(a) para apagar o quadro!'.format(aluno_sorteado))


#Desafio 020 - Aula 08 - Mundo 1 (Ordem aleatória)

from random import shuffle

aluno1 = input('Qual o nome do aluno 1? ')
aluno2 = input('Qual o nome do aluno 2? ')
aluno3 = input('Qual o nome do aluno 3? ')
aluno4 = input('Qual o nome do aluno 4? ')

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)

print('A ordem de apresentação é: {}'.format(lista))

#Desafio 021 - Aula 08 - Mundo 1 (Tocar MP3)

'''from tkinter import *
import pygame

caixa = Tk()
caixa.title('MP3')
caixa.geometry('250x250')

pygame.mixer.init()

def play():
    pygame.mixer.music.load('C:/Users/viito/Downloads/Naruto Soundtrack- Sadness and Sorrow (FULL VERSION).mp3')
    pygame.mixer.music.play(loops=0)

play_button = Button(caixa, text='Tocar música!', command=play)
play_button.pack(pady=20)

def stop():
    pygame.mixer.music.stop()

stop_button = Button(caixa, text='Parar música!', command=stop)
stop_button.pack(pady=20)

caixa.mainloop()'''


#Desafio 022 - Aula 09 - Mundo 1 (Leitura do nome completo e características)

nome = input('Digite o seu nome: ')

nome_upper = nome.upper()
nome_lower = nome.lower()

nome_sem_espaco = nome.replace(' ', '')
len_nome = len(nome_sem_espaco)

lista = nome.split(' ')
primeiro_nome = lista[0]
len_primeiro_nome = len(primeiro_nome)

print('Seu nome com todas as letras maiúsculas é: {}'.format(nome_upper))
print('Seu nome com todas as letras minúsculas é: {}'.format(nome_lower))
print('Seu nome tem {} letras'.format(len_nome))
print('Seu primeiro nome, que é {}, tem {} letras'.format(primeiro_nome, len_primeiro_nome))


#Desafio 023 - Aula 09 - Mundo 1 (Digitos separados)

num = str(input('Digite um número de 0 à 9999: ')) #Forcei a ser string pra utilizar os
                                                   #métodos de string

if len(num) >= 5:
    print('O número tem mais de 4 algarismos!')
    num = str(input('Por favor, digite um número de 0 à 9999: '))
    while len(num) >= 5:
        num = str(input('Por favor, digite um número de 0 à 9999: '))

if len(num) == 1:
    unidade = num[0]
    print('A unidade do número {} é: {}!'.format(num, unidade))
    
elif len(num) == 2:
    unidade = num[1]
    dezena = int(num[0])
    print('A unidade do número {} é: {}!'.format(num, unidade))
    print('A dezena do número {} é: {}!'.format(num, dezena * 10))
    
elif len(num) == 3:
    unidade = num[2]
    dezena = int(num[1])
    centena = int(num[0])
    print('A unidade do número {} é: {}!'.format(num, unidade))
    print('A dezena do número {} é: {}!'.format(num, dezena * 10))
    print('A centena do número {} é: {}!'.format(num, centena * 100))
    
elif len(num) == 4:
    unidade = num[3]
    dezena = int(num[2])
    centena = int(num[1])
    milhar = int(num[0])
    print('A unidade do número {} é: {}!'.format(num, unidade))
    print('A dezena do número {} é: {}!'.format(num, dezena * 10))
    print('A centena do número {} é: {}!'.format(num, centena * 100))
    print('O milhar do número {} é: {}!'.format(num, milhar * 1000))

 
#Desafio 024 - Aula 09 - Mundo 1 (Condicional para string)

cidade = str(input('Qual o nome da cidade? '))

cidade_padronizada = cidade.lower()

lista = cidade_padronizada.split()

if lista[0] == 'santo':
    print('O nome da cidade começa com a palavra Santo!')
else:
    print('O nome da cidade não começa com a palavra Santo!')
    

#Desafio 025 - Aula 09 - Mundo 1 (Procurando uma string específica)

nome = str(input('Qual o seu nome? '))

nome_padronizado = nome.strip().lower()

silva = nome_padronizado.find('silva')

if silva == -1:
    print('Seu nome não tem Silva!')
else:
    print('Seu nome tem Silva!')
    

#Desafio 026 - Aula 09 - Mundo 1 (Procurando e contando determinado caractere)

frase = str(input('Escreva a frase que você deseja analisar: '))

frase_padronizada = frase.strip().lower()

num_a = frase_padronizada.count('a')
if num_a > -1:
    
    if num_a == 1: #Singular
        print('Quantas vezes a letra "a" aparece? {} vez'.format(num_a))
    elif num_a > 1: #Plural
        print('Quantas vezes a letra "a" aparece? {} vezes'.format(num_a))
else:
    print('Quantas vezes a letra "a" aparece? A frase não apresenta a letra "a"')

prim_a = frase_padronizada.find('a')
if prim_a > -1:
    print('Em qual posição a letra "a" aparece pela primeira vez? Na posição {}'.format(prim_a + 1)) #+1 para que seja coerente com uma contagem começando do 1
else:
    print('Em qual posição a letra "a" aparece pela primeira vez? A frase não apresenta a letra "a"')

ultima = int()
for i in range(0, len(frase_padronizada)):
    letra = frase_padronizada[i]
    if letra == 'a':
        ultima = i
        
if ultima == 0:
    print('Em qual posição a letra "a" aparece pela última vez? A frase não apresenta a letra "a"')
else:
    print('Em qual posição a letra "a" aparece pela última vez? Na posição {}'.format(ultima + 1))


#Desafio 027 - Aula 09 - Mundo 1 (Primeiro e último nome)

nome = str(input('Digite o seu nome: '))

nome_formatado = nome.strip().lower()

lista = nome_formatado.split()

primeiro_nome = lista[0]
ultimo_nome = lista[(len(lista) - 1)]

if primeiro_nome != ultimo_nome:
    print('Seu primeiro nome é {} e seu último nome é {}'.format(primeiro_nome.capitalize(), ultimo_nome.capitalize()))
else:
    print('Seu primeiro nome, {}, é igual ao seu último nome'.format(primeiro_nome.capitalize()))


#Desafio 028 - Aula 10 - Mundo 1 (Jogo de adivinhação)

import random

num_pc = random.randint(0, 5) #Número inteiro aleatório de 0 a 5

num_usuario = int(input('Escolha um número: '))

if num_usuario == num_pc:
    print('Parabéns, você acertou o número misterioso!')
    denovo = input('Gostaria de tentar novamente (S/N)? ')
    while denovo == 'S':
        num_pc = random.randint(0, 5)
        
        num_usuario = int(input('Escolha um número: '))
        
        if num_usuario == num_pc:
            print('Parabéns, você acertou o número misterioso!')
            denovo = input('Gostaria de tentar novamente (S/N)? ')
        else:
            print('Que pena, o número misterioso era {}. Você não acertou!'.format(num_pc))
            denovo = input('Gostaria de tentar novamente (S/N)? ')
else:
    print('Que pena, o número misterioso era {}. Você não acertou!'.format(num_pc))
    denovo = input('Gostaria de tentar novamente (S/N)? ')
    while denovo == 'S':
        num_pc = random.randint(0, 5)
        
        num_usuario = int(input('Escolha um número: '))
        
        if num_usuario == num_pc:
            print('Parabéns, você acertou o número misterioso!')
            denovo = input('Gostaria de tentar novamente (S/N)? ')
        else:
            print('Que pena, o número misterioso era {}. Você não acertou!'.format(num_pc))
            denovo = input('Gostaria de tentar novamente (S/N)? ')


#Desafio 029 - Aula 10 - Mundo 1 (Multa de trânsito)

velocidade = float(input('Qual a velocidade registrada em Km/h? '))
limite = 80

if velocidade <= limite:
    print('Velocidade permitida! Parabéns pela responsabilidade!')
else:
    acima = (velocidade - limite) #Quantos Km/h acima do limite
    print('Velocidade acima do permitido!\nVelocidade permitida: {} Km/h\nVelocidade registrada: {:.0f} Km/h'.format(limite, velocidade))
    valor_multa = (acima * 7) #7 reais por Km/h acima do limite
    print('O motorista deve ser multado em R$ {:.2f}'.format(valor_multa))
    
    
#Desafio 030 - Aula 10 - Mundo 1 (Par ou ímpar?)

num = int(input('Digite um número inteiro e descubra se ele é par ou ímpar: '))

if (num % 2) == 0:
    print('{} é par!'.format(num))
else:
    print("{} é ímpar!".format(num))


#Desafio 031 - Aula 10 - Mundo 1 (Preço da passagem)

dist = float(input('Qual a distância, em Km, da sua viagem? '))

if dist <= 200:
    preco = (0.5 * dist)
else:
    preco = (0.45 * dist)

print('O preço da sua passagem é: R$ {:.2f}'.format(preco))


#Desafio 032 - Aula 10 - Mundo 1 (Ano bissexto)

ano = int(input('Digite o ano e vou te dizer se ele é bissexto: '))

if ((ano % 100) == 0) and ((ano % 400) != 0):
    print('O ano {} não é bissexto'.format(ano))
elif (ano % 4) == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

##Bônus - Como pegar a data atual do sistema

from datetime import date

print(date.today())
print(date.today().year)
print(date.today().month)
print(date.today().day)


#Desafio 033 - Aula 10 - Mundo 1 (Qual é o maior?)

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

bol_1 = num1 > num2
bol_2 = num1 > num3
bol_3 = num2 > num3

if bol_1 == True and bol_2 == True and bol_3 == True:
    maior = num1
    menor = num3

elif bol_1 == False and bol_2 == True and bol_3 == True:
    maior = num2
    menor = num3

elif bol_1 == False and bol_2 == False and bol_3 == True:
    maior = num2
    menor = num1

elif bol_1 == False and bol_2 == False and bol_3 == False:
    maior = num3
    menor = num1
    
elif bol_1 == True and bol_2 == True and bol_3 == False:
    maior = num1
    menor = num2

elif bol_1 == True and bol_2 == False and bol_3 == False:
    maior = num3
    menor = num2
    
print('O maior número é {:.2f} e o menor {:.2f}'.format(maior, menor))


#Desafio 034 - Aula 10 - Mundo 1 (Aumento salarial)

salario = float(input('Boa tarde proletário sofredor! Qual o seu salário? '))

if salario > 1250:
    novo_salario = (salario * 1.1)
    print('Parabéns, você receberá um aumento de 10%!\nSeu novo salário é: R$ {:.2f}'.format(novo_salario))
else:
    novo_salario = (salario * 1.15)
    print('Parabéns, você receberá um aumento de 15%!\nSeu novo salário é: R$ {:.2f}'.format(novo_salario))


#Desafio 035 - Aula 10 - Mundo 1 (Essas retas formam um triângulo?)

##O comprimento de a deve ser menor que b + c e assim sucessivamente

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print('As retas podem formar um triângulo :)')
else:
    print('As retas não podem formar um triângulo :(')