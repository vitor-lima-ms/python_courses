#Módulos

##Math

import math

#Ou

#from math import ... #Dessa forma, não precisamos utilizar a sintaxe math.função

###Arredondamentos

x = 7.6

y = math.ceil(x) #Arredonda pra cima
print(y)

y = math.floor(x) #Arredonda pra baixo
print(y)


###Trunc

x = 1.2367

y = math.trunc(x) #Elimina as casas decimais sem arredondamento
print(y)


###Sqrt

x = 81

y = math.sqrt(x) #Raiz quadrada
print(y)


###Factorial

x = 3

y = math.factorial(x) #Calcula o fatorial n!
print(y)