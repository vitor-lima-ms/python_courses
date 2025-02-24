#Funcao
def estatistica_notas(*notas, situacao=False):
    """Funcao para analisar notas e a situacao da amostra de alunos.
    :param notas: Uma ou mais notas dos alunos.
    :param situacao (Opcional): Retorna um valor categorico com base na media das notas.
    :return: Retorna um dicionario com as metricas calculadas"""
    dicionario_notas = {}
    dicionario_notas['Total de notas'] = len(notas)
    maior_nota = 0
    menor_nota = 999
    soma_nota = 0
    for nota in notas:
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
        soma_nota += nota
    media_nota = soma_nota / len(notas)
    dicionario_notas['Maior nota'] = maior_nota
    dicionario_notas['Menor nota'] = menor_nota
    dicionario_notas['Media'] = media_nota
    if situacao == True:
        if media_nota < 5:
            dicionario_notas['Situacao'] = 'Ruim'
        elif 5 <= media_nota < 7:
            dicionario_notas['Situacao'] = 'Razoavel'
        else:
            dicionario_notas['Situacao'] = 'Boa'
    return dicionario_notas


#Programa principal
resultado = estatistica_notas(2, 7, 4, situacao=True)
print(resultado)
help(estatistica_notas)