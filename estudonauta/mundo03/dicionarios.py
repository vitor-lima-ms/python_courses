'''Mais uma forma de variavel composta, alem das tuplas e listas'''
#Podemos personalizar os indices dos dicionarios
#a = dict() ou a = {}
#append nao funciona
pessoa = {
    'nome': 'Vitor',
    'idade': '24'
}
print(pessoa)
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos') #Como usamos aspas simples no print formatado, devemos usar aspas duplas dentro dos colchetes
pessoa['sexo'] = 'M' #Simples de adicionar mais dados
print(pessoa)
del(pessoa['idade']) #Forma de remover dados
print(pessoa)
#nome, idade e sexo sao chaves
print(pessoa.keys())
#valores sao Vitor, 24 e M
print(pessoa.values())
#Itens sao a juncao da chave com o valor
print(pessoa.items()) #Os items sao retornados como tuplas dentro de uma lista
for k, v in pessoa.items():
    print(f'O {k} e {v}')
#Podemos criar listas com dicionarios dentro
familia = [{
    'nome': 'Vitor',
    'idade': '24'
},{
    'nome': 'Geraldo',
    'idade': '64'
},{
    'nome': 'Simone',
    'idade': '55'
},{
    'nome': 'Maria',
    'idade': '23'
}]
print(familia)
print(familia[0]) #Acessando o dicionario
print(familia[0]['idade']) #Acessando a idade dentro do dicionario
print(type(familia[0]['idade']))
print(type(int(familia[0]['idade']))) #Mas podemos converter os itens de um dicionario

estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)

#Nova funcionalidade -> .copy() -> mesma coisa do [:] para listas
estado = {}
brasil = []
for i in range(0, 3):
    estado['nome'] = input('Digite o nome de um estado: ')
    estado['sigla'] = input('Digite a sigla desse estado: ')
    brasil.append(estado.copy())
    estado.clear()
print(brasil)
for estado in brasil:
    for k, v in estado.items():
        print(f'O campo {k} tem valor {v}')

'''Em strings formatadas, sera necessario utilizar aspas duplas para utilizar as chaves dos dicionarios'''

#Ordenando dicionarios
from operator import itemgetter
x = {
    'a1': 10,
    'a2': 5,
    'a3': 7,
    'a4': 8
}
print(x)
y = {}
y = sorted(x.items(), key=itemgetter(1),) #itemgetter pega a chave ou o valor. 0 para chave e 1 para valor
print(y) #Retorna uma lista ordenada cujos items sao tuplas com a chave e o valor -> Para acessar: lista[0][0] ou lista[0][1] etc.