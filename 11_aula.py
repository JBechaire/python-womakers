# operadores relacionais e precedência de operadores

# operadores relacionais
# exemplos de operadores relacionais: ==, !=, >, <, >=, <=
# Maior que: >
# menor que: <
# maior ou igual a: >=  
# menor ou igual a: <=
# igual a: ==   
# diferente de: !=
# exemplo de uso dos operadores relacionais
a = 10  
b = 20
print(a > b)  # False
print(a < b)  # True
print(a >= b)  # False
print(a <= b)  # True
print(a == b)  # False
print(a != b)  # True   
print(a == 10)  # True
print(a != 10)  # False 
print("+++++++++++++++" \
"++++++++++++++++++++++++++++++")

valorA = input("Digite o valor de A: ")
valorB = input("Digite o valor de B: ")

print(valorA > valorB)  # comparação de strings
print(valorA < valorB)  # comparação de strings 
print(valorA >= valorB)  # comparação de strings
print(valorA <= valorB)  # comparação de strings    
print(valorA == valorB)  # comparação de strings
print(valorA != valorB)  # comparação de strings    
print("+++++++++++++++" \
"++++++++++++++++++++++++++++++")

# precedência de operadores
# a ordem de avaliação dos operadores em uma expressão é determinada pela precedência dos operadores

# exemplo de expressão com operadores de diferentes precedências
resultado = 10 + 20 * 3  # multiplicação tem precedência sobre adição
print(resultado)  # 10 + (20 * 3) = 10 + 60 = 70    
resultado = (10 + 20) * 3  # parênteses alteram a precedência
print(resultado)  # (10 + 20) * 3 = 30 * 3 = 90
resultado = 10 + 20 * 3 - 5  # multiplicação tem precedência sobre adição e subtração
print(resultado)  # 10 + (20 * 3) - 5 = 10 + 60 - 5 = 65
resultado = 10 + 20 * (3 - 5)  # parênteses alteram a precedência
print(resultado)  # 10 + 20 * (3 - 5) = 10 + 20 * (-2) = 10 - 40 = -30  

valorA = input("Digite o valor de A: ")
valorB = input("Digite o valor de B: ")
resultado = valorA + valorB * 2   # multiplicação tem precedência sobre adição
print(resultado)  # concatenação de strings: valorA + (valorB * 2)
resultado = (valorA + valorB) * 2  # parênteses alteram a precedência
print(resultado)  # concatenação de strings: (valorA + valorB) * 2

print("+++++++++++++++" \
"++++++++++++++++++++++++++++++")

valorA = input("Digite o valor de A: ")
valorB = input("Digite o valor de B: ")
#resultado = valorA + valorB > 2 
print(resultado)  # comparação de strings: (valorA + valorB) > 2

print("+++++++++++++++" \
"++++++++++++++++++++++++++++++")

# ================================
# OPERADORES RELACIONAIS E PRECEDÃŠNCIA
# ================================

# Exemplos de operadores relacionais:
# >   maior que
# <   menor que
# >=  maior ou igual
# <=  menor ou igual
# ==  igual a
# !=  diferente de

# input() recebe valores como TEXTO
# int() converte o texto para nÃºmero inteiro
valorA = int(input("Qual Ã© o valor A? "))
valorB = int(input("Qual Ã© o valor B? "))


# ================================
# TESTES RELACIONAIS (comentados)
# ================================

# Podemos testar cada operador individualmente:
# print(valorA > valorB)   # True se valorA for maior que valorB
# print(valorA < valorB)   # True se valorA for menor que valorB
# print(valorA >= valorB)  # True se valorA for maior ou igual a valorB
# print(valorA <= valorB)  # True se valorA for menor ou igual a valorB
# print(valorA == valorB)  # True se valorA for igual a valorB
# print(valorA != valorB)  # True se valorA for diferente de valorB


# ================================
# EXEMPLO DE PRECEDÃŠNCIA
# ================================

# O Python respeita a ordem das operaÃ§Ãµes:
# Primeiro sÃ£o feitas as somas, subtraÃ§Ãµes, multiplicaÃ§Ãµes etc.
# Depois as comparaÃ§Ãµes
resultado = valorA + valorB > 2

# Exibe o resultado do teste lÃ³gico
# True ou False
print(resultado)


