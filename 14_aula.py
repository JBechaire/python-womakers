#retindo tarefas com  WHILE
# EXEMPLO 1

contador = 0

while contador < 3:
    contador += 1
    print(contador, 'Olá!')
    print('+++++++++++')

# EXEMPLO 2
tentativas = 3
while tentativas > 0:
    resposta = input('Qual é a capital do Brasil? ')
    if resposta.lower() == 'brasilia':
        print('Resposta correta!')
        break
    else:
        tentativas -= 1
        print(f'Resposta incorreta. Você tem {tentativas} tentativas restantes.')
else:    print('Suas tentativas acabaram. A resposta correta é Brasília.')
print('Fim do programa.')
print('+++++++++++')

# diferente do for, o while não tem um contador automático, por isso é necessário criar uma variável para controlar o número de iterações.
# o while é útil quando não sabemos de antemão quantas vezes queremos repetir um bloco de código, ou quando queremos repetir algo até que uma condição seja satisfeita. Já o for é mais adequado para iterar sobre uma sequência de elementos, como listas ou strings, ou para repetir um bloco de código um número específico de vezes.
# O while é mais flexível, mas também pode ser mais propenso a erros, como loops infinitos, se a condição de parada não for corretamente definida ou atualizada dentro do loop. Por isso, é importante ter cuidado ao usar o while e garantir que haja uma condição de parada clara.
# O while é uma estrutura de controle de fluxo que permite repetir um bloco de código enquanto uma condição for verdadeira. Ele é útil quando não sabemos de antemão quantas vezes queremos repetir um bloco de código, ou quando queremos repetir algo até que uma condição seja satisfeita. Já o for é mais adequado para iterar sobre uma sequência de elementos, como listas ou strings, ou para repetir um bloco de código um número específico de vezes. O while é mais flexível, mas também pode ser mais propenso a erros, como loops infinitos, se a condição de parada não for corretamente definida ou atualizada dentro do loop. Por isso, é importante ter cuidado ao usar o while e garantir que haja uma condição de parada clara.

# ================================
# REPETIÃ‡ÃƒO DE TAREFAS COM WHILE EM PYTHON
# ================================

# ================================
# VARIÃVEL DE CONTROLE
# ================================

tentativas = 3  # quantidade de tentativas disponÃ­veis

# ================================
# LOOP WHILE
# ================================

# Enquanto o nÃºmero de tentativas for maior que 0, o loop continua
while tentativas > 0:
    # Exibe a quantidade de tentativas restantes
    print("VocÃª ainda tem ", tentativas, " tentativas!")
    
    # Decrementa 1 na variÃ¡vel de controle para evitar loop infinito
    tentativas -= 1

# ================================
# FORA DO LOOP
# ================================

# Quando o while termina, esta linha Ã© executada
#print("Fora do loop")
