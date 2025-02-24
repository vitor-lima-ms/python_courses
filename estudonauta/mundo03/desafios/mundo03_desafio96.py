#Funcao
def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área do seu terreno de {largura}m de largura e {comprimento}m de comprimento e {area_terreno}m2.')


#Programa principal
largura_terreno = float(input('Qual a largura do terreno [m]? '))
comprimento_terreno = float(input('Qual o comprimento do terreno [m]? '))
area(largura_terreno, comprimento_terreno)