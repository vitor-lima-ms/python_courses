'''A modularizacao surgiu para facilitar a criacao de codigos que envolvem um numero relativamente grande de variaveis, 
operacoes etc. Foco -> Dividir programas, aumentar a legibilidade e facilitar a manutencao'''

#Exemplo 1
##Funcoes
def fatorial(numero):
    fat = 1
    for numeros in range(1, numero + 1):
        fat *= numeros
    return fat
def dobro(numero):
    dobro = numero * 2
    return dobro
def triplo(numero):
    triplo = numero * 3
    return triplo


#Programa principal
numero_usuario = int(input('Digite um numero: '))
print(f'O fatorial de {numero_usuario} e {fatorial(numero_usuario)}.')
print(f'O dobro de {numero_usuario} e {dobro(numero_usuario)}.')
print(f'O triplo de {numero_usuario} e {triplo(numero_usuario)}.')

#Exemplo modularizado
import mundo03.modulos_pacotes.exemplos.defs_mod as dmod
#from defs import fatorial, dobro, triplo #Nao muito recomendado

numero_usuario = int(input('Digite um numero: '))
print(f'O fatorial de {numero_usuario} e {dmod.fatorial(numero_usuario)}.')
print(f'O dobro de {numero_usuario} e {dmod.dobro(numero_usuario)}.')
print(f'O triplo de {numero_usuario} e {dmod.triplo(numero_usuario)}.')

'''Qualquer arquivo .py pode ser um modulo'''

'''Vantagens da modularizacao:
1- Organizacao do codigo
2- Facilita a manutencao
3- Ocultacao do codigo detalhado
4- Reutilizacao em projetos'''

#Quando os modulos nao sao suficientes, podemos usar pacotes (conhecidos como bibliotecas em outras linguagens)
'''Se os modulos ficam muito grandes, os problemas voltam a aparecer.
Para contornar isso, podemos criar um conjunto de modulos em um diretorio -> Pacote'''
#import biblioteca
#from biblioteca import grupo_modulos
#Nas pastas dos pacotes, e necessario que haja um arquivo __init__.py -> Nele, ficam as funcoes

import defs_lib as dlib
numero_usuario = int(input('Digite um numero: '))
print(f'O fatorial de {numero_usuario} e {dlib.fatorial(numero_usuario)}.')
print(f'O dobro de {numero_usuario} e {dlib.dobro(numero_usuario)}.')
print(f'O triplo de {numero_usuario} e {dlib.triplo(numero_usuario)}.')