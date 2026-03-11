#condições com if, elif e else
#traduzindo para português: se, senão se e senão
#exemplo 1

print(10 > 5) #true
print(10 < 5) #false
if 10 > 5:
    print("10 é maior que 5")
else:
    print("10 não é maior que 5")
#exemplo 2
idade = 18
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você não é maior de idade")

#exemplo 3
idade = 65
idoso = True
if idade >= 60 and idoso:
    print("Você tem direito a  30% de desconto para idosos")
else:    print("Você não tem direito a desconto para idosos")

#exemplo 4
nota = 85   
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
else:
    print("C")

#exemplo 5
numero = 10        
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

 #exemplo 6
nota1 = 3.0
nota2 = 8.0    
nota3 = 6.0   

media = (nota1 + nota2 + nota3) / 3
if media >= 7.0:
    print("Aprovado, Nota: ",round(media, 1))   
elif media >= 5.0:
    print("Recuperação, Nota: ", round(media, 1))   
else:    print("Reprovado, Nota: ", round(media, 1))

# ================================
# CONDIÃ‡Ã•ES ANINHADAS COM IF, ELSE E ELIF EM PYTHON
# ================================

# Dados da pessoa
idade = 60           # idade da pessoa
e_membro = False     # verifica se a pessoa Ã© membro de algum clube/associaÃ§Ã£o

# ================================
# CONDIÃ‡ÃƒO PRINCIPAL
# ================================

# if: verifica se a idade Ã© maior ou igual a 60
if idade >= 60:

    # CONDIÃ‡ÃƒO ANINHADA
    # Verifica se a pessoa Ã© membro
    if e_membro:
        # Se for membro, aplica desconto maior
        print("30% de desconto")
    else:
        # Se nÃ£o for membro, aplica desconto menor
        print("20% de desconto")

# elif: verifica se a idade Ã© maior ou igual a 50 (mas menor que 60)
elif idade >= 50:
    # Se estiver nessa faixa etÃ¡ria, oferece outro benefÃ­cio
    print("Vale compras com cashback")

# else: para todas as outras situaÃ§Ãµes
else:
    # NÃ£o hÃ¡ desconto ou benefÃ­cio
    print("Sem desconto!")

    
# ================================
# CONDIÃ‡Ã•ES COM IF, ELIF E ELSE EM PYTHON
# ================================

# Notas de uma aluna
nota1 = 10
nota2 = 6
nota3 = 7.5

# ================================
# CÃLCULO DA MÃ‰DIA
# ================================

# Soma das notas dividida pela quantidade de notas
media = (nota1 + nota2 + nota3) / 3

# ================================
# CONDIÃ‡ÃƒO IF / ELIF / ELSE
# ================================

# if: verifica a primeira condiÃ§Ã£o
if media >= 7:
    # Se a mÃ©dia for maior ou igual a 7, a aluna estÃ¡ aprovada
    # round() limita a exibiÃ§Ã£o da mÃ©dia a 2 casas decimais
    print("Aprovada - NOTA: ", round(media, 2))

# elif: verifica uma segunda condiÃ§Ã£o se o if nÃ£o foi verdadeiro
elif media >= 5:
    # Se a mÃ©dia for maior ou igual a 5 e menor que 7, a aluna estÃ¡ em recuperaÃ§Ã£o
    print("RecuperaÃ§Ã£o - NOTA: ", round(media, 2))

# else: executa quando nenhuma das condiÃ§Ãµes anteriores Ã© verdadeira
else:
    # Se a mÃ©dia for menor que 5, a aluna estÃ¡ reprovada
    print("Reprovada - NOTA: ", round(media, 2))

