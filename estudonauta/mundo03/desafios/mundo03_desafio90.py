aluno = {}
aluno['nome'] = input('Nome de aluno: ')
aluno['media'] = input('Media: ')
if float(aluno['media']) > 7:
    aluno['situacao'] = 'Aprovado'
elif float(aluno['media']) > 5 and float(aluno['media']) < 7:
    aluno['situacao'] = 'Recuperacao'
elif float(aluno['media']) < 5:
    aluno['situacao'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k.capitalize()} = {v}')