#Desafio 004 - Aula 06 - Mundo 1 (Características de um valor qualquer)

qualquer_coisa = input('Digite qualquer coisa: ')

print('É alfanumérica?', qualquer_coisa.isalnum())
print('É alfabética?', qualquer_coisa.isalpha())
print('É decimal?', qualquer_coisa.isdecimal())
print('Está apenas com letras minúsculas?', qualquer_coisa.islower())
print('É numérica?', qualquer_coisa.isnumeric())
print('É um espaço em branco?', qualquer_coisa.isspace())
print('Está apenas com letras maiúsculas?', qualquer_coisa.isupper())
print('Está capitalizada?', qualquer_coisa.istitle())
