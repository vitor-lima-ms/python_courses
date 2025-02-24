from time import sleep
#Funcao
def contador(inicio, fim, passo):
    if passo == 0 and fim > inicio:
        print(f'Contagem de {inicio} ate {fim} com passo 1')
        for numero in range(inicio, (fim + 1), 1):
            sleep(0.25)
            print(numero, end=' ', flush=True)
    elif passo == 0 and fim < inicio:
        print(f'\nContagem de {inicio} ate {fim} com passo -1')
        for numero in range(inicio, (fim - 1), -1):
            sleep(0.25)
            print(numero, end=' ', flush=True)
    elif fim > inicio:
        print(f'\nContagem de {inicio} ate {fim} com passo {passo}')
        for numero in range(inicio, (fim + 1), passo):
            sleep(0.25)
            print(numero, end=' ', flush=True)
    elif fim < inicio and passo > 0:
        print(f'\nContagem de {inicio} ate {fim} com passo {passo}')
        for numero in range(inicio, (fim - passo), (-passo)):
            sleep(0.25)
            print(numero, end=' ', flush=True)
    elif fim < inicio and passo < 0:
        print(f'\nContagem de {inicio} ate {fim} com passo {passo}')
        for numero in range(inicio, (fim + passo), passo):
            sleep(0.25)
            print(numero, end=' ', flush=True)    


#Programa principal
contador(1, 10, 1) #Contador de 1-10 com passo 1
contador(10, 0, 2) #Contador de 10-0 com passo 2
inicio_usuario = int(input('\nInicio: '))
fim_usuario = int(input('Fim: '))
passo_usuario = int(input('Passo: '))
contador(inicio_usuario, fim_usuario, passo_usuario)