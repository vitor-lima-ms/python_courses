tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um numero entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Por favor, digite um numero entre 0 e 20: '))
print(f'O numero digitado escrito por extenso e: {tupla[num]}')