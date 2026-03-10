#trabalhando com strings
nome = "Joselaine" 

print(nome[0]) #imprime a letra J
print(nome[1]) #imprime a letra o
print(nome[0:4]) #imprime a letra Jose
print(nome[5:]) #imprime a palavra laine

frase = "Quanto mais estudo, mais sinto que minha mente  é insaciável por conhecimento"
print (frase)

frase = """\"Quanto mais estudo, 
mais sinto que minha 
mente é insaciável
por conhecimento\" """

print (frase)


frase = '''"Quanto mais estudo, 
mais sinto que minha 
mente é insaciável
por conhecimento\" '''

print (frase)

# ================================
# TRABALHANDO COM TEXTOS (string)
# ================================

# Aqui estamos criando uma variÃ¡vel do tipo string (texto)
# Usamos trÃªs aspas simples (''') para criar um texto de mÃºltiplas linhas
# Isso permite quebrar linhas sem precisar usar \n
frase = '''"Quanto mais estudo,
mais sinto que minha mente
nisso Ã© insaciÃ¡vel"'''

# print() exibe o conteÃºdo da variÃ¡vel no terminal
# O texto serÃ¡ mostrado exatamente como foi escrito
print(frase)
