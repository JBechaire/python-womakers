# comentarios em python
# isso é um comentário de linha única
print("Olá, mundo!")  # isso é um comentário após uma linha de código


"""
isso é um comentário de múltiplas linhas
que pode se estender por várias linhas  
e é útil para explicar blocos de código ou fornecer documentação
"""

# ================================
# Mensagem de abertura
# ================================

# print() Ã© usado para exibir mensagens no terminal
# Aqui estamos apenas mostrando uma saudaÃ§Ã£o inicial
print("Oi!")


# ================================
# ExibiÃ§Ã£o de mensagem e entrada de dados
# ================================

# input() pausa o programa e espera a pessoa digitar algo
# O valor digitado serÃ¡ armazenado na variÃ¡vel nome
nome = input("Qual Ã© o seu nome? ")  # Captura de nome


# ================================
# ContinuaÃ§Ã£o da execuÃ§Ã£o do programa
# ================================

# Aqui mostramos uma mensagem de boas-vindas
# A vÃ­rgula permite juntar texto fixo com o valor da variÃ¡vel
print("Seja bem vinda: ", nome)

# Esta linha imprime uma mensagem simples
# Ela NÃƒO gera erro de execuÃ§Ã£o, apenas exibe o texto
print("este Ã© um erro!")


# ================================
# ComentÃ¡rio de mÃºltiplas linhas
# ================================

'''
Este Ã© um comentÃ¡rio
de mÃºltiplas linhas.

Ele pode ser usado para:
- ExplicaÃ§Ãµes longas
- AnotaÃ§Ãµes
- DocumentaÃ§Ã£o do cÃ³digo

Tudo que estiver aqui dentro
NÃƒO serÃ¡ executado pelo Python.
'''


# ================================
# Entrada e exibiÃ§Ã£o da idade
# ================================

# Pedimos a idade da pessoa usuÃ¡ria
# Mesmo sendo um nÃºmero, o input() retorna TEXTO (string)
idade = input("Qual Ã© a sua idade? ")

# Exibimos a idade no terminal
# Neste momento, ainda nÃ£o fazemos cÃ¡lculos com ela
print('Sua idade Ã©: ', idade)