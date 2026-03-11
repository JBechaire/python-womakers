# ================================
# TRATAMENTO DE ERROS EM PYTHON
# ================================

# Bloco try/except para tratar erros em operaçoes matematematicas
# O bloco try tenta executar o codigo
# Se ocorrer um erro, o Python procura um except correspondente


try:
    # Captura um numero digitado pelo usuario
    numero = int(input("Digite um numero: "))
    
    # Tenta dividir 10 pelo numero informado
    resultado = 10 / numero
    
except ZeroDivisionError:
    # Este bloco executa se o usuario digitar 0
    print("Não é possivel dividir por ZERO!")

except ValueError:
    # Este bloco executa se o usuario digitar algo que nao seja numero
    print("Digite somente numero")

else:
    # Este bloco executa somente se não ocorrer nenhum erro
    print(f"Resultado: {resultado}")


# ================================
# TRATAMENTO DE ERROS COM ARQUIVOS
# ================================

try:
    # Tenta abrir o arquivo 'dados.txt' no modo leitura
    arquivo = open("dados.txt", mode="r")
    
    #  conteudo do arquivo
    conteudo = arquivo.read()

except FileNotFoundError:
    # Executa se o arquivo não existir
    print("Arquivo não encontrado")

finally:
    # Este bloco sempre executa, aconteça erro ou não
    print("Operação finalizada")