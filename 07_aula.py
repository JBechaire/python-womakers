#numeros decimais -FLOAT
preco = 2.0
temperatura = -3.14
mediaNotas = 7.5

preco = input("Valor do produto: ") #este é uma string, mesmo que o usuario digite um numero, ele vai ser tratado como string
preco_prociononal = float(input("Valor Promocional: "))

print("A diferença de valor  é: ",round(float(preco) -preco_prociononal, 2)) #este é um numero decimal, mesmo que o usuario digite um numero inteiro, ele vai ser tratado como decimal, e o resultado da subtração também será um numero decimal, e o round() é usado para arredondar o resultado para 2 casas decimais

# ================================
# NÃšMEROS DECIMAIS (float)
# ================================

# VariÃ¡veis do tipo float podem ser positivas ou negativas
temperatura = -3.14
media_notas = 7.5

# Este print tambÃ©m estÃ¡ comentado
# print("Valor por minuto: ", int(preco))


# ================================
# ENTRADA DE DADOS E CONVERSÃƒO
# ================================

# input() sempre retorna TEXTO (string)
# Aqui ainda NÃƒO fazemos a conversÃ£o
preco = input("Valor normal por minuto: ")

# Aqui jÃ¡ convertemos diretamente para float
# Usamos float porque o valor pode ter casas decimais
preco_promocional = float(input("Valor promocional: "))


# ================================
# OPERAÃ‡ÃƒO MATEMÃTICA
# ================================

# Para fazer a conta, precisamos converter 'preco' para float
# SubtraÃ­mos o valor promocional
# round(..., 2) limita o resultado a duas casas decimais
print("DiferenÃ§a de valor: ", round(float(preco) - preco_promocional, 2))