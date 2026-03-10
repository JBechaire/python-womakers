# numeros interos
escola = 12
aulasRealizadas = 35
alunos =23

print("codigos de escola: ", escola)
print("aulas realizadas: ", aulasRealizadas)
print("numero de alunos: ", alunos)

#este não é um numero inteiro, é uma string
escola = "12"

#este NÃO é um numero inteiro
preco = 2.50 


print("valor por minuto: ", int(preco))#este é um numero inteiro

#precoProciononal = int(input("Valor Promocional: "))
preco_prociononal = int(float(input("Valor Promocional: "))) #este é um numero inteiro, mesmo que o usuario digite um numero com virgula, ele vai converter para inteiro

print("Valor promocional por minuto é: ", preco_prociononal)

# ================================
# NÃšMEROS INTEIROS (int)
# ================================

# Estas variÃ¡veis armazenam nÃºmeros inteiros
# int representa nÃºmeros SEM casas decimais
escola = 12
aulas_realizadas = 35
alunos = 23

# Exibimos vÃ¡rias informaÃ§Ãµes em um Ãºnico print()
# A vÃ­rgula separa os valores e adiciona espaÃ§os automaticamente
print(
    "CÃ³digo da Escola: ", escola,
    "Aulas realizadas: ", aulas_realizadas,
    "Alunos: ", alunos
)


# ================================
# NÃšMEROS DECIMAIS (float)
# ================================

# Este NÃƒO Ã© um nÃºmero inteiro
# Ã‰ um nÃºmero decimal, do tipo float
preco = 2.50

# Convertendo float para int
# O int() REMOVE as casas decimais (nÃ£o arredonda)
print("Valor por minuto: ", int(preco))


# ================================
# CONVERSÃƒO COM INPUT()
# ================================

# input() sempre retorna TEXTO (string)
# Primeiro convertemos para float (por causa do decimal)
# Depois convertemos para int
preco_promocional = int(float(input("Valor promocional: ")))

# Exibimos o valor final convertido
print("Valor promocional por minuto: ", preco_promocional)