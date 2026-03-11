#LISTAS EM PYTHON
# As listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável. Elas são mutáveis, o que significa que podemos modificar seus elementos após a criação. As listas são definidas usando colchetes [] e os elementos são separados por vírgulas.
# ================================
# REPETIÇÃO DE TAREFAS COM WHILE EM PYTHON
# ================================
#EXEMPLO 1
cursos = ['Python', 'Git', 'JavaScript', 'Java', 'C#']

#imprime a lista completa e cada elemento individualmente, além de mostrar como modificar um elemento, adicionar um novo elemento e remover um elemento da lista.
print(cursos)
print(cursos[0])  # Acessando o primeiro elemento da lista
print(cursos[1])  # Acessando o segundo elemento da lista  
print("================================")

#alterando um elemento da lista
cursos[1] = 'Git e GitHub'  # Modificando o segundo elemento da lista
print(cursos)
print("================================")
#adicionando um novo elemento à lista
cursos.append('SQL')  # Adicionando um novo elemento ao final da lista
print(cursos)
print("================================")

 #removendo um elemento da lista   
cursos.remove('C#')  # Removendo um elemento da lista
print(cursos)
print("================================")

#Removendo um elemento usando o índice
cursos.remove('Java')  # Removendo um elemento da lista
cursos.pop(2)  # Removendo o elemento no índice 2 (JavaScript)
print(cursos)
print("================================")

# ================================
# LISTAS EM PYTHON
# ================================

# Lista de cursos
cursos = ["Python", "Git", "Design", "CV"]

# ================================
# EXIBINDO LISTAS
# ================================

# Mostra a lista inteira
print(cursos)

# Mostra apenas o segundo elemento (Ã­ndice 1)
# Lembre-se: o Ã­ndice comeÃ§a em 0
print(cursos[1])

# ================================
# ALTERANDO ELEMENTOS
# ================================

# Substitui o valor do Ã­ndice 1 por outro valor
cursos[1] = "Git e GitHub"
print(cursos)

# ================================
# ADICIONANDO ELEMENTOS
# ================================

# Adiciona um novo item ao final da lista
cursos.append("Dados")
print(cursos)

# ================================
# REMOVENDO ELEMENTOS
# ================================

# Remove pelo valor do item
cursos.remove("Design")

# Remove pelo Ã­ndice (primeiro elemento)
cursos.pop(0)

# Lista atualizada
print(cursos)

