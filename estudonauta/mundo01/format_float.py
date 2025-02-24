#Desafio 03 - Formatando floats

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma = num1 + num2

print('O resultado da soma entre {} e {} é {}'.format(num1, num2, soma))

print('O resultado da soma entre {} e {} é {:.3f}'.format(num1, num2, soma)) #Mostra apenas 3 casas decimais após a vírgula

print('O resultado da soma entre {} e {} é {:.3f}'.format(num1, num2, soma), end=' ') #Não quebra a linha de um print para o outro
print('Estou na mesma linha')

print('O resultado da \n soma entre {} e {} é {:.3f}'.format(num1, num2, soma)) #\n quebra a linha
