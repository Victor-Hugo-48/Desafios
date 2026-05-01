# DESAFIO 5 - GERAR MATRIZ COM NÚMEROS ALEATÓRIOS

import random
import numpy as np

print("\n=== MÉTODO 1 - USANDO RANDOM ===")

# Criando matriz vazia
matriz = []

# Definindo tamanho da matriz
num_linhas = 3
num_colunas = 3

# Intervalo dos números
min_valor = 0
max_valor = 9

# Preenchendo a matriz
for i in range(num_linhas):  # percorre linhas
    linha = []  # cria nova linha
    
    for j in range(num_colunas):  # percorre colunas
        numero = random.randint(min_valor, max_valor)  # gera número aleatório
        linha.append(numero)  # adiciona na linha
    
    matriz.append(linha)  # adiciona linha na matriz

# Mostrando matriz
print("Matriz gerada com random:")
for linha in matriz:
    print(linha)


print("\n=== MÉTODO 2 - USANDO NUMPY ===")

# Definindo intervalo (no numpy o max NÃO é incluído)
min_valor = 0
max_valor = 10

# Gerando matriz automaticamente
matriz_np = np.random.randint(min_valor, max_valor, size=(3, 3))

# Mostrando matriz
print("Matriz gerada com NumPy:")
print(matriz_np)