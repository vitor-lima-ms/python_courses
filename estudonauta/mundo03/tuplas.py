#Sao variaveis compostas que sao imutaveis. Podemos muda-la apenas
    #quando interrompemos o programa
#Cada elemento recebe um indice
#Podemos fazer slicing tb

x = (1, 2, 3, 4)

print(x[3]) #Ultimo elemento
print(x[-1]) #Tb o ultimo elemento. -2 e o penultimo e assim sucessivamente
print(len(x)) #Tamanho da tupla

for i in range(len(x)): #Printa todos os elementos da tupla
    print(x[i])
for i in x: #Tb printa todos os termos
    print(i)
for c, v in enumerate(x): #enumerate mostra o element0 referente ao indice e a posicao dele na variavel composta
    print(c, v)
print(sorted(x)) #Ordena os elementos de uma variavel. No caso de tuplas, e criada uma lista com os itens da tupla
                    #ordenados

y = (1, 2, 3, 4)
print(y[0])
y[0] = 0 #Vai dar erro pois n podemos mudar elementos de uma tupla

a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = a + b
print(c) #Nao soma os elementos
d = b + a
print(d) #d e diferente de c. A ordem importa

a = (4, 5, 4, 4, 9, 9)
print(a.count(4)) #Conta quantas vezes um elemento aparece
print(a.index(5)) #Retorna o indice do elemento. Quando o mesmo elemento aparece mais de uma vez, retorna o menor indice
print(a.index(4, 1)) #Se soubermos que o um elemento aparece em um determinado indice, podemos utilizar
                                        #um argumento adicional para definir de onde a procura ira comecar
pessoa = ('Vitor', 24, 'Homem') #Tuplas aceitam variaveis de formatos diferentes
print(f'Ola! Me chamo {pessoa[0]}, tenho {pessoa[1]} anos e sou {pessoa[2].lower()}')
del(pessoa) #Apaga todos os elementos de uma tupla ou qualquer outra variavel. Podemos usas del(variavel[indice])
                #para apagar os elementos de outras variaveis compostas, menos de uma tupla, ja que ela e imutavel
print(pessoa)

a = (4, 5, 4, 4, 9, 9)
print(max(a)) #Maior valor de uma tupla
print(min(a)) #Menor valor de uma tupla