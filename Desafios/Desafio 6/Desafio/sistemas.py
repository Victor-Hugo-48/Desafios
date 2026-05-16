import numpy as np  # Biblioteca para trabalhar com matrizes

# Listas onde vou guardar os dados
A = []
B = []

print("=== Sistema 3x3 ===")

# Entrada da matriz A
print("\nDigite os valores da matriz A:")

for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"A[{i}][{j}]: "))
        linha.append(valor)
    A.append(linha)

# Entrada do vetor B
print("\nDigite os valores do vetor B:")

for i in range(3):
    valor = float(input(f"B[{i}]: "))
    B.append(valor)

# Convertendo para numpy
A = np.array(A)
B = np.array(B)

try:
    # Verificando se a matriz pode ser resolvida
    det = np.linalg.det(A)

    if abs(det) < 1e-10:
        print("\nErro: a matriz A não pode ser invertida (determinante zero).")
    else:
        # Resolvendo o sistema
        X = np.linalg.solve(A, B)

        # Mostrando a matriz A
        print("\nMatriz A:")
        for i in range(3):
            for j in range(3):
                print(f"{A[i][j]:.0f}", end=" ")
            print()

        # Mostrando vetor B
        print("\nVetor B:")
        print(B)

        # Mostrando solução
        print("\nSolução do sistema:")
        print(f"x = {X[0]:.2f}")
        print(f"y = {X[1]:.2f}")
        print(f"z = {X[2]:.2f}")

except np.linalg.LinAlgError:
    print("\nErro ao resolver o sistema (matriz inválida).")