#operações especiais

#exemplo de operador de atribuição composto
# +=  INCREMENTO é um operador de atribuição composto que adiciona o valor à variável e atribui o resultado de volta à variável.
#-= DECREMENTO é um operador de atribuição composto que subtrai o valor da variável e atribui o resultado de volta à variável.
#*= é um operador de atribuição composto que multiplica o valor da variável e atribui o resultado de volta à variável.
# /= é um operador de atribuição composto que divide o valor da variável e atribui o resultado de volta à variável. 

valorA = int(input("Digite um valor A: "))
valorB = int(input("Digite um valor B: "))

valorA += 0
valorB -= 2

print("Valor A após incremento: ", valorA)
print("Valor B após decremento: ", valorB)
print("++++++++++++++++++++++++++++++++++++++++++++")

if valorA % 2 == 0:
    print("Valor A é par.")
else:
    print("Valor A é ímpar.")

print("++++++++++++++++++++++++++++++++++++++++++++")    

# ================================
# OPERAÃ‡Ã•ES ESPECIAIS EM PYTHON
# ================================

# Exemplos de operadores especiais:
# +=  incremento (soma e atualiza a variÃ¡vel)
# -=  decremento (subtrai e atualiza a variÃ¡vel)
# %   resto da divisÃ£o


# ================================
# ENTRADA DE DADOS
# ================================

# input() recebe valores como TEXTO
# int() converte o texto para nÃºmero inteiro
valorA = int(input("Qual Ã© o valor A? "))
valorB = int(input("Qual Ã© o valor B? "))


# ================================
# OPERAÃ‡Ã•ES COM ATRIBUIÃ‡ÃƒO
# ================================

# Esta linha estÃ¡ comentada, entÃ£o NÃƒO serÃ¡ executada
# Se fosse executada, somaria 5 ao valor atual de valorA
# valorA += 5

# Aqui subtraÃ­mos 2 do valor atual de valorB
# Ã‰ o mesmo que escrever: valorB = valorB - 2
valorB -= 2


# ================================
# EXIBIÃ‡ÃƒO DOS VALORES
# ================================

# Mostramos os valores finais apÃ³s as operaÃ§Ãµes
print("valor final A: ", valorA)
print("valor final B: ", valorB)


# ================================
# VERIFICAÃ‡ÃƒO DE NÃšMERO PAR OU ÃMPAR
# ================================

# Usamos o operador % para verificar o resto da divisÃ£o por 2
# Se o resto for 0, o nÃºmero Ã© par
if valorA % 2 == 0:
    print("NÃºmero par")
else:
    # Se o resto for diferente de 0, o nÃºmero Ã© Ã­mpar
    print("NÃºmero Ã­mpar")