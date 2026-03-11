# Manipulando arquivos em Python
import os 
arquivo = "19_exercicioAula.txt"
alunas = []

with open(arquivo,mode="w",encoding="utf-8") as lista:
    lista.write("1. Ana\n")
    lista.write("2. Betina\n")
    lista.write("3. Caroline\n") 


#lendo o arquivo
'''
with open(arquivo,mode="r", encoding="utf-8") as lista:
    conteudo = lista.read()
print(conteudo)
'''

#lendo o arquivo linha por linha
'''
with open(arquivo,mode="r", encoding="utf-8") as lista:
    for linha in lista:
        print(linha.strip())
'''

# lendo arquivo
'''
with open(arquivo,mode="r", encoding="utf-8") as lista:
   linhas = lista.readlines()

print(linhas)   
'''
'''
with open(arquivo,mode="r", encoding="utf-8") as lista:
    for linhas in lista.readlines():
        alunas.append(linhas.strip())
        
print(alunas)
     

with open(arquivo,mode="r", encoding="utf-8") as lista:
   alunas = lista.readlines()
   
alunas_atualizadas = []   

for aluna in alunas:
    nome = aluna.strip()

    if nome != "Caroline":
        alunas_atualizadas.append(nome)

# Sobrescrevemos o arquivo com os nomes atualizados
with open(arquivo, mode="w", encoding="utf-8") as lista:
  for aluna in alunas_atualizadas:
       lista.write(aluna + "\n")

with open(arquivo, mode="a", encoding="utf-8") as lista:
     lista.write("4. Daniela")
     '''
if os.path.exists(arquivo):
    os.remove(arquivo)
    print("Arquivo Excluído!")   
else: 
    print("Arquivo não encontrado")


# ================================
# MANIPULAÃ‡ÃƒO DE ARQUIVOS EM PYTHON
# ================================


#Importamos o mÃ³dulo os para trabalhar com o sistema operacional
 #Ele permite verificar se o arquivo existe e deletÃ¡-lo


# Nome do arquivo que vamos manipular
#arquivo = "alunas.txt"

# Lista para armazenar nomes de alunas (pode ser usada para leitura ou atualizaÃ§Ã£o)
#alunas = []

# ================================
# CRIAÃ‡ÃƒO E ESCRITA DE ARQUIVO
# ================================
# Comentei para nÃ£o sobrescrever o arquivo toda vez que rodar
# with open(arquivo, mode="w", encoding="utf-8") as lista:
#     # Cada write() adiciona uma nova linha no arquivo
#     lista.write("Ana\n")
#     lista.write("Beatriz\n")
#     lista.write("Gisele\n")

# ================================
# LEITURA DO ARQUIVO
# ================================
# Leitura completa do arquivo como uma Ãºnica string
# with open(arquivo, mode="r", encoding="utf-8") as lista:
#     conteudo = lista.read()

# Leitura linha por linha com strip() para remover \n
# with open(arquivo, mode="r", encoding="utf-8") as lista:
#     for linha in lista:
#         print(linha.strip())

# ================================
# LEITURA PARA LISTA
# ================================
# Cada linha do arquivo vira um item da lista
# with open(arquivo, mode="r", encoding="utf-8") as lista:
#     alunas = lista.readlines()

# ================================
# ATUALIZANDO O ARQUIVO
# ================================
# Criamos uma nova lista para armazenar apenas os nomes que queremos manter
# alunas_atualizadas = []

# for aluna in alunas:
#     nome = aluna.strip()  # Remove espaÃ§os e \n
#     if nome != "Gisele":  # Remove "Gisele"
#         alunas_atualizadas.append(nome)

# Sobrescrevemos o arquivo com os nomes atualizados
# with open(arquivo, mode="w", encoding="utf-8") as lista:
#     for aluna in alunas_atualizadas:
#         lista.write(aluna + "\n")

# ================================
# ADICIONANDO NOVOS NOMES
# ================================
# with open(arquivo, mode="a", encoding="utf-8") as lista:
#     lista.write("Daniela\n")  # Adiciona ao final do arquivo

# ================================
# DELETANDO O ARQUIVO
# ================================
# Verifica se o arquivo existe antes de tentar remover
#if os.path.exists(arquivo):
#   os.remove(arquivo)  # Remove o arquivo do sistema
#    print("Arquivo removido!")
#else:
#  print("Arquivo nÃ£o encontrado")
