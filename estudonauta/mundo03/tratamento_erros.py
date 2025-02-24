'''Erros = Problemas de sintaxe. Excecoes = ValueError, ZeroDivisionError, TypeError, IndexError, KeyError
ModuleNotFoundError etc.'''

#Exemplo 1
try: #Tente -> Obrigatoria
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    resultado = a / b
except: #Se der erro, faca tal coisa -> Obrigatoria
    print('Infelizmente tivemos um problema!')
else: #Se n der erro, faca tal coisa -> Opcional
    print(f'O resultado e {resultado:.2f}')
finally: #Acontence independente de erro ou nao -> Opcional
    print('Volte sempre!')

#Exemplo 2
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    resultado = a / b
except Exception as erro: #Permite exibir o erro na saida padrao. Podemos passar varios argumentos como .__class__ etc.
    print(f'Infelizmente tivemos um problema: {erro.__class__}')
else:
    print(f'O resultado e {resultado:.2f}')
finally:
    print('Volte sempre!')

#Exemplo 3 - Um mesmo try pode ter varios except
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    resultado = a / b
except (ValueError, TypeError):
    print('Infelizmente tivemos um problema com os tipos de dados que vc utilizou.')
except ZeroDivisionError:
    print('Nao e possivel dividir por 0.')
except KeyboardInterrupt:
    print('O usuario preferiu interromper.')
except Exception as erro:
    print(f'A causa do erro foi: {erro.__cause__}')
else:
    print(f'O resultado e {resultado:.2f}.')
finally:
    print('Volte sempre!')