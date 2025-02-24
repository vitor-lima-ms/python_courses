produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

'''Ordenar os produtos por nome decrescente e gerar uma variavel produtos_ordenados_por_nome por deep copy'''

def ordena_por_nome(produto):
    return produto['nome']

ordenamento = sorted(produtos, key=ordena_por_nome, reverse=True)

from copy import deepcopy

produtos_ordenados_por_nome = deepcopy(ordenamento)

print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')