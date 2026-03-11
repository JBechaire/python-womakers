#repetindo tarefas FOR
#repetir uma tarefa um número específico de vezes
#exemplo 1
n = 4
for i in range(0, n):
    print("Repetição", i)
print("+++++++++++")

#exemplo 2
nome = "Python"
for letra in nome:
    print(letra)
print("+++++++++++")

#exemplo 3
tecnologias = ["Python", "Java", "C++", "JavaScript"]
for item in tecnologias:
    print(item)
print("+++++++++++")

#exemplo 4
perfil = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
for chave in perfil:
    print(chave, ":", perfil[chave])
    print("+++++++++++")

#exemplo 5
tecnologias = ["Python", "Java", "C++", "JavaScript"]
for item in range(len(tecnologias)):
    print(tecnologias[item])
print("+++++++++++")

#exemplo 6
for indice in range(5):
    print("Repetição", indice)
    print("oi,gurias")
    print("+++++++++++")

#exemplo 7
indice = 0
for item in range(3):
    indice += item
    print("numero atual", indice) 
    print("+++++++++++")
    # ================================
# REPETIÃ‡ÃƒO DE TAREFAS COM FOR EM PYTHON
# ================================

# ================================
# EXEMPLOS DE FOR COM LISTAS (comentado)
# ================================

# Lista de tecnologias
# tecnologias = ["Python", "Dados", "IA"]

# Percorre cada Ã­ndice da lista usando range e len
# for item in range(len(tecnologias)):
#     print(tecnologias[item])

# ================================
# EXEMPLO DE FOR COM DICIONÃRIOS (comentado)
# ================================

# Perfil de uma pessoa
# perfil = { "nome": "Ana", "estado": "RS"}

# Percorre cada chave do dicionÃ¡rio
# for chave in perfil:
#     print(chave, perfil[chave])

# ================================
# EXEMPLO DE FOR COM RANGE SIMPLES (comentado)
# ================================

# for indice in range(5):
#     print("Repetindo!", indice)
#     print("Oie, WoMakers!")

# ================================
# EXEMPLO PRÃTICO COM ACUMULADOR
# ================================

indice = 0  # inicializa a variÃ¡vel acumuladora

# Percorre os nÃºmeros de 0 a 4
for item in range(5):
    # Soma o item ao Ã­ndice acumulador
    indice += item
    # Exibe o valor atual do acumulador
    print("NÃºmero atual", indice)
    



   
