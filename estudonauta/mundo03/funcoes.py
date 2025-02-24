'''Em todas as linguagens de programacao, as funcoes estao associadas a palavra rotina.
Rotina = Processos repetitivos.
print(), len(), int() sao funcoes que ja existem no Python.
Para processos repetitivos que n tem uma funcao nativa associada, podemos criar a funcao'''
def mostralinha(): #Sempre def + nome da funcao (arbitrario) + ():
    print('-' * 5)


#Programa principal. Sempre duas linhas apos a def
mostralinha()
mostralinha()
mostralinha()

#Parametros
def mensagem(msg): #Parametro(s) -> Variaveis que estao dentro do parenteses
    print('-' * 5)
    print(msg)
    print('-' * 5)


mensagem('Teste') #Chamando a funcao com o parametro 'Teste'

#Exemplo 1
##Funcao
def soma(num1, num2):
    print(f'a = {num1} e b = {num2}')
    resultado_soma = num1 + num2
    return resultado_soma
    #Pode ser print(resultado_soma) tb

##Programa principal
soma(1, 1)
soma(num1=1, num2=3) #Podemos especificar qual parametro e qual

#Exemplo 2 - Empacotamento de parametros
##Funcao
def contador(*num): #O simbolo de * significa desempacotar. O usuario pode passar varios parametros dessa forma. Cria uma tupla com os argumentos
    tamanho = len(num)
    print(tamanho)
    for numero in num:
        print(f'{numero} ', end='')


contador(1, 2, 3, 4)
contador(10, 20, 30, 40, 50)
contador(100, 200, 300, 400, 500, 600)

def soma(*num):
    somatorio = 0
    for numero in num:
        somatorio += numero
    print(somatorio)


soma(1, 2, 3)
soma(4, 5, 6)

#Exemplo 3 - Trabalhando com listas
valores  = [1, 2, 3 ,4 ,5]
def dobra(lista):
    indice = 0
    while indice < len(lista):
        lista[indice] *= 2
        indice += 1
    
valores_dobrados = valores[:]
dobra(valores_dobrados)
print(valores)
print(valores_dobrados)

#Interactive help
help() #Utilizado para consultar a documentacao das funcoes nativas do python
help(print)

#docstrings -> Strings de documentacao
print(input.__doc__) #Nao e a mesma coisa do help mas tb ajuda

'''As funcionalidades acima so funcionam para funcoes nativas do Python. Contudo, podemos criar docstrings para as nossas
funcoes'''

def area(largura, comprimento):
    """Calcula a area de retangulos.
    param largura:  largura do retangulo
    param comprimento: comprimento do retangulo
    return: sem retorno"""
    area_terreno = largura * comprimento
    print(f'A área do seu terreno de {largura}m de largura e {comprimento}m de comprimento e {area_terreno}m2.')

help(area)

#Parametros opcionais
def somar(a, b, c=0): #Parametros com =0 sao opcionais
    soma = a + b + c
    print(f'{soma}')


somar(1, 2, 3)
somar(4, 5)

def somar(a=0, b=0, c=0): #Parametros com =0 sao opcionais
    soma = a + b + c
    print(f'{soma}')


somar()

#Escopo de variaveis
'''Local onde as variaveis vao existir dentro do programa'''
##Funcao
def teste():
    y = 2
    print(f'Na funcao x vale {x}')
    print(f'Na funcao y vale {y}')

##Programa principal
x = 1
teste()
print(f'No programa principal x vale {x}')
#print(f'No programa principal y vale {y}') #Da um erro
'''x e uma variavel global equanto y tem um escopo local'''

'''Podemos declarar uma mesma variavel global e localmente. Isso tambem e valido para importacao de bibliotecas'''
##Funcao
def teste():
    x = 1
    print(f'Na funcao x vale {x}')


##Programa principal
x = 2
teste()
print(f'No programa principal x vale {x}')

'''Quando usamos o global, o Python utiliza a variavel global dentro do escopo, nao criando uma variavel local'''
##Funcao
def teste():
    global x
    x = 1
    print(f'Na funcao x vale {x}')


##Programa principal
x = 2
teste()
print(f'No programa principal x vale {x}')

#Retornando valores
def somar(a=0, b=0, c=0):
    soma = a + b + c
    return soma #Facilita a formatacao posterior. Podemos retornar strings, valores booleanos, tuplas, listas etc.


x = somar(1, 2, 3)
y = somar(4, 5)
z = somar(10)
print(f'As somas valem {x}, {y} e {z}')
print(f'A soma de 1, 2 e 3 vale {somar(1, 2, 3)}') #Nao precisamos necessariamente colocar o return dentro de uma variavel

#Exemplo 1
def fatorial(numero=1): #Tornamos o numero como parametro opcional. Se ele nao for informado, seu valor sera 1
    fat = 1
    for numeros in range (1, (numero + 1)):
        fat *= numeros
    return fat


x = fatorial(5)
print(x)
'''Com mais de uma parametro sendo retornado pelo return, a funcao retorna um tupla'''

#Diferenca entre print e return
##Quando uso print -> Nao preciso atribuir o resultado a uma variavel ou utilizar diretament no print formatado fora da
##funcao, apenas chamar a funcao

##Quando uso return -> Preciso atribuir a uma variavel ou utilizar diretamente no print formatado -> Da uma maior liberdade
##para formatar a exibicao dos resultados