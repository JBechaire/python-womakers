#Dicionario de Dados em Python
#Os dicionários em Python são estruturas de dados que armazenam pares de chave-valor

#EXEMPLO 1
aluno = {"nome": "Ana",
         "idade": 22,
         "curso": "Python",
         "status": "ativo"}
print(aluno)
print(aluno["nome"]) #Acessando o valor associado à chave "nome"
print(aluno["idade"]) #Acessando o valor associado à chave "idade"

aluno["idade"] = 23 #Alterando o valor associado à chave "idade"
print(aluno["idade"]) #Acessando o valor atualizado associado à chave "idade"
aluno["cidade"] = "São Paulo" #Adicionando uma nova chave-valor ao dicionário
print(aluno)

aluno.pop("status") #Removendo a chave "status" do dicionário
print(aluno)
print("========================================")

#diferenca entre tuplas e dicionários
#As tuplas são imutáveis, ou seja, não podem ser alteradas depois   de criadas, enquanto os dicionários são mutáveis, permitindo a adição, remoção e modificação de elementos. As tuplas são definidas usando parênteses () e os dicionários são definidos usando chaves {}. As tuplas são indexadas por posição, enquanto os dicionários são indexados por chaves.
#Difernça entre dicionario e lista
#As listas são ordenadas e mutáveis, permitindo a adição, remoção e modificação de elementos. Os dicionários são mutáveis e permitem acesso aos valores através de chaves, enquanto as listas permitem acesso aos elementos através de índices.

#EXEMPLO 2- LISTAS DE DICIONÁRIOS
escola = [
    {"nome": "Ana", "idade": 22, "curso": "Python", "status": "ativo"},    
    {"nome": "Carla", "idade": 25, "curso": "Java", "status": "ativo"},
    {"nome": "Maria", "idade": 30, "curso": "JavaScript", "status": "inativo"}
]
print(escola)
print(escola[0]) #Acessando o primeiro dicionário da lista
print("========================================")
for aluno in escola:
    print(aluno["nome"]) #Acessando o valor associado à chave "nome" de cada dicionário na lista

for aluno in escola:
    print(f"Nome:{aluno['nome']},")
    print(f"Curso:{aluno['curso']},")
    print("="*40)

    # ================================
# DICIONÃRIOS E LISTAS DE DADOS EM PYTHON
# ================================

# Lista chamada 'escola' que contÃ©m dicionÃ¡rios
# Cada dicionÃ¡rio representa uma aluna com seus atributos
escola = [
    {
        "nome": "Ana",
        "idade": 45,
        "curso": "Python",
        "status": True  # True significa ativa, False inativa
    },
    {
        "nome": "Cynthia",
        "idade": 34,
        "curso": "C#",
        "status": True
    },
    {
        "nome": "Clarice",
        "idade": 23,
        "curso": "Dados",
        "status": False
    }
]

# ================================
# ACESSANDO ELEMENTOS
# ================================

# Podemos acessar uma aluna pelo Ã­ndice da lista
# aluna = escola[2]
# print(aluna)

# Mostra toda a lista de dicionÃ¡rios
# print(escola)

# ================================
# PERCORRENDO A LISTA COM FOR
# ================================

# Aqui usamos um for para percorrer cada dicionÃ¡rio dentro da lista
for aluna in escola:
    # Verifica se o nome da aluna Ã© "Cynthia"
    if aluna["nome"] == "Cynthia":
        # Exibe informaÃ§Ãµes da aluna encontrada
        print(f"Nome: {aluna['nome']}")
        print(f"Curso: {aluna['curso']}")

# ================================
# EXPLICAÃ‡Ã•ES DIDÃTICAS
# ================================

# 1. Cada item da lista 'escola' Ã© um dicionÃ¡rio
# 2. Cada dicionÃ¡rio contÃ©m pares chave:valor (ex: "nome":"Ana")
# 3. Para acessar um valor, usamos aluna["nome"] ou aluna["curso"]
# 4. Podemos filtrar ou aplicar condiÃ§Ãµes usando if dentro do for

