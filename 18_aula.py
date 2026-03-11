#FUNÇÕES

#EXEMPLO 1
def saudacao():
    print("Olá, seja bem vinda!")

saudacao()
print("=="*20)

#EXEMPLO 2

def saudacao(nome,estado):
    print(f"Olá, seja bem vinda {nome} do estado {estado}!")

saudacao("Josy","RS")
print("=="*20)

#EXEMPLO 3

def soma(a,b):
    return a + b
resultado = soma(5,3)
print(resultado)
print("=="*20)

#EXEMPLO 4
def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
idade_usuario = int(input("Digite sua idade: "))
resultado = verificar_idade(idade_usuario)
print(resultado)
print("=="*20)
# ================================
# FUNÃ‡Ã•ES EM PYTHON
# ================================

# FunÃ§Ã£o que exibe uma saudaÃ§Ã£o personalizada
# Ela recebe dois parÃ¢metros: nome e estado
def saudacao(nome, estado):
    # f-string permite inserir variÃ¡veis dentro do texto
    print(f"{nome}, Seja bem vinda. Muito bom ver alguÃ©m de {estado}")


# FunÃ§Ã£o que retorna a soma de dois nÃºmeros
# Recebe dois parÃ¢metros: a e b
def soma(a, b):
    # return devolve o resultado para quem chamou a funÃ§Ã£o
    return a + b


# FunÃ§Ã£o que verifica se a pessoa Ã© maior de idade
# Recebe um parÃ¢metro: idade
def verificar_idade(idade):
    # Condicional para verificar se idade >= 18
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
    
# ================================
# EXECUTANDO FUNÃ‡Ã•ES
# ================================

# Chamando a funÃ§Ã£o verificar_idade com valor 18
# A funÃ§Ã£o retorna uma string que serÃ¡ exibida pelo print
print(verificar_idade(18))

# Exemplos adicionais:
# saudacao("Cynthia", "SP")  -> Exibe: Cynthia, Seja bem vinda. Muito bom ver alguÃ©m de SP
# print(soma(10, 5))          -> Exibe: 15


