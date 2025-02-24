#Manipulação textual

texto = 'Vitor Lima de Miranda e Silva' #Essa variável é alocada em um determinado
                                        #espaço da memória. Contudo, cada caractere é
                                        #armazenado individualmente em 'pequenas subdivisões'
                                        #do espaço de memória no qual a variável foi 
                                        #armazenada
                                        
##Fatiamento (slicing)

print(texto[9]) #Letra 'a' de 'Lima'

print(texto[0:5]) #'Vitor'. O primeiro '[' é inclusivo. O segundo '[', não

print(texto[0:9:2]) #Vai do índice 0 ao 8 de dois em dois

print(texto[:5]) #Quando omitimos o início, ele sempre parte do índice 0

print(texto[5:]) #Quando omitimos o final, ele sempre vai até o último índice

print(texto[5::2]) #Começa do índice 5, vai até o último índice de dois em dois


##Análise

print(len(texto)) #Comprimento da string

print(texto.count('a')) #Quantas vezes a letra 'a' aparece na string
print(texto.count('A')) #Case sensitive
print(texto.count('a', 0, 10)) #Conta quantas vezes a letra 'a' aparece entre o índice
                               #0 e o índice 9

print(texto.find('ima')) #Retorna em qual índice a cadeia 'ima' começa
print(texto.find('Branco')) #Retorna -1 quando a cadeia não é encontrada na string

print('Vitor' in texto) #Se a cadeia for encontrada na string, retorna True


##Transformação

print(texto.replace('Vitor', 'Geraldo')) #Substitui uma cadeia de caracterees ou um caractere
                                         #por outra cadeia ou caractere

print(texto.upper()) #Troca as letra minúsculas por maiúsculas. Bom para padronização

print(texto.lower()) #Contrário do .lower(). Bom para padronização

print(texto.capitalize()) #Apenas o primeiro caractere será maiúsculo

print(texto.title()) #Onde tem espaço, faz uma quebra de palavras. Cada palavra
                     #identificada terá a primeira letra como maiúscula

texto = '   Vitor Lima de Miranda e Silva '
print(texto)
print(texto.strip()) #Remove espaços em branco inúteis

texto = '   Vitor Lima de Miranda e Silva '
print(texto.rstrip()) #Remove somente os espaços à direita

texto = '   Vitor Lima de Miranda e Silva '
print(texto.lstrip()) #Remove somente os espaços à esquerda

##Divisão

texto = 'Vitor Lima de Miranda e Silva'

texto_sep = texto.split()
print(texto_sep) #Divide a string e retorna uma lista.
                 #Por padrão, divide nos espaços em branco
                 
print(texto_sep[0][0]) #Retorna o primeiro caractere do primeiro item da lista
                    
print(' '.join(texto_sep)) #Junta uma lista de strings separando-as com o
                           #delimitador especificado
                           
##Print de grandes cadeias de caracteres

print("""Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto
      Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto 
      Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto """)
#Usar """

## Os métodos podem ser combinados

print(texto.upper().count('I'))