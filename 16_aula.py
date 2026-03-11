#TUPLAS EM PYTHON
#As tuplas são imutáveis, ou seja, não podem ser alteradas depois de criadas. Elas são definidas usando parênteses () e podem conter elementos de diferentes tipos de dados.
#Exemplo de tupla
dias_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
print(dias_semana)
print(dias_semana[0]) #Acessando o primeiro elemento da tupla
print(dias_semana[3]) #Acessando o quarto elemento da tupla
print("========================================")
#As tuplas também podem ser usadas para armazenar dados relacionados, como coordenadas geográficas, informações de contato, etc.

#Exemplo de tupla com diferentes tipos de dados
coordenadas = (40.7128, -74.0060)  # Coordenadas de Nova York
print(coordenadas)
print("========================================")
#As tuplas também podem ser usadas para armazenar dados relacionados, como coordenadas geográficas, informações de contato, etc.    
#Exemplo de tupla com diferentes tipos de dados
contato = ("João", "joao@email.com", "(11) 99999-9999")
print(contato)
print("========================================")
#As tuplas também podem ser usadas para armazenar dados relacionados, como coordenadas geográficas, informações de contato, etc.
#Exemplo de tupla com diferentes tipos de dados
pessoa = ("Maria", 30, "Engenheira")
print(pessoa)
print("========================================")

# ================================
# TUPLAS EM PYTHON
# ================================

# Tupla com os dias da semana
# Tuplas sÃ£o semelhantes a listas, mas os valores NÃƒO podem ser alterados depois de criados
dias_da_semana = ("segunda", "terÃ§a", "quarta", "quinta", "sexta")

# Tupla com coordenadas
# Ideal para dados fixos que nÃ£o mudam
coordenadas = (10, 20)

# ================================
# ACESSANDO ELEMENTOS
# ================================

# Mostra o primeiro elemento da tupla (Ã­ndice 0)
# Lembre-se: o Ã­ndice comeÃ§a em 0
print(coordenadas[0])

# Mostra todos os dias da semana
print(dias_da_semana)

# Mostra o Ãºltimo dia usando Ã­ndice negativo
print(dias_da_semana[-1])
