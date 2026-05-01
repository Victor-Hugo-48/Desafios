# Desafio 4  - MATRIZES EM PYTHON - EXERCÍCIOS PRÁTICOS

# Importação das bibliotecas
import random          # Usado para gerar números aleatórios
import numpy as np     # Usado para operações com matrizes

# EXERCÍCIO 1 - MATRIZ 3x3 COM ZEROS E ALEATÓRIOS
print("\n=== EXERCÍCIO 1 ===")

# Cria matriz 3x3 corretamente
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(random.randint(1, 10))
    matriz.append(linha)

# Exibe a matriz final
print("Matriz 3x3 com números aleatórios:")
for linha in matriz:
    print(linha)

# EXERCÍCIO 2 - SOMA DE MATRIZES (VENDAS)
print("\n=== EXERCÍCIO 2 ===")

# Matrizes representando vendas
vendas1 = [
    [100, 200],
    [150, 250]
]

vendas2 = [
    [50, 100],
    [100, 150]
]

# Cria matriz resultado com zeros
resultado = [[0, 0], [0, 0]]

# Soma elemento por elemento das duas matrizes
for i in range(2):      # linhas
    for j in range(2):  # colunas
        resultado[i][j] = vendas1[i][j] + vendas2[i][j]

# Exibe o resultado da soma
print("Soma das matrizes de vendas:")
for linha in resultado:
    print(linha)

# EXERCÍCIO 3 - MÉDIA DOS ALUNOS (NUMPY)
print("\n=== EXERCÍCIO 3 ===")

# Matriz onde cada linha representa um aluno
# e cada coluna representa uma nota
alunos = np.array([
    [7, 8, 9],
    [6, 5, 7],
    [10, 9, 8]
])

# Calcula a média de cada linha (cada aluno)
medias = np.mean(alunos, axis=1)

# Exibe as médias
print("Médias dos alunos:")
for i, media in enumerate(medias):
    print(f"Aluno {i+1}: {media:.2f}")

# EXERCÍCIO 4 - DETERMINANTE DA MATRIZ
print("\n=== EXERCÍCIO 4 ===")

# Matriz 3x3 (coeficientes de um sistema linear)
matriz_det = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

# Calcula o determinante da matriz
det = np.linalg.det(matriz_det)

# Exibe o valor do determinante
print("Determinante:", det)

# Verifica se o sistema tem solução única
if det != 0:
    print("Sistema POSSUI solução (matriz invertível)")
else:
    print("Sistema NÃO possui solução única")

# EXERCÍCIO 5 - TRANSPOSIÇÃO E MULTIPLICAÇÃO
print("\n=== EXERCÍCIO 5 ===")

# Matriz de estoque (quantidade de produtos)
estoque = np.array([
    [10, 20],
    [30, 40]
])

# Matriz de preços dos produtos
precos = np.array([
    [2, 3],
    [4, 5]
])

# Transpõe a matriz (troca linhas por colunas)
transposta = estoque.T

# Multiplica as matrizes para calcular valores totais
resultado = np.dot(transposta, precos)

# Exibe os resultados
print("Matriz transposta:")
print(transposta)

print("Resultado da multiplicação:")
print(resultado)