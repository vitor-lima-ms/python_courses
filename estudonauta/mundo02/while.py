#While

'''Estrutura de controle com teste lógico'''

'''Enquanto a condição não for atendida,
o laço não é interrompido'''

'''Quando não soubermos o limite,
utilizamos o while'''

##Utilizando for

for i in range(1, 10):
    print(i)
print('Fim!')

##Utilizando while

i = 1

while i < 10:
    print(i)
    i = i + 1
print('Fim!')

##Resultados iguais!

##Exemplo 1 - Condição de parada

i = 1

while i != 0:
    i = int(input('Digite o valor de i: '))
print('Fim!')
    
    
#Exemplo 2

r = 's'

while r == 's':
    n = int(input('Digite um valor: '))
    r = input('Quer continuar [s/n]? ').lower()
    while r != 's' and r != 'n':
        print('Valor inválido!')
        r = input('Por favor, escolha entre s ou n: ')

print('Fim!')


#Exemplo 3

n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print('Quantidade de números inteiros pares: {}'.format(par))      
print('Quantidade de números inteiros ímpares: {}'.format(impar))

##O 0 nesse caso foi analisado

n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um número inteiro: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1

print('Quantidade de números inteiros pares: {}'.format(par))      
print('Quantidade de números inteiros ímpares: {}'.format(impar))

#Interrompendo while --> break






    
    
    
    
    






   

    















