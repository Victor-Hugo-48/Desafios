import numpy as np  # Importa a NumPy

# Matriz dos coeficientes
A = np.array([
    [4, 2, 3],
    [3, 3, 2],
    [5, 1, 4]
])

# Vetor de resultados
B = np.array([150, 140, 160])

try:
    # Verifica determinante (boa prática do exercício)
    det = np.linalg.det(A)
    print(f"Determinante da matriz: {det:.4f}")

    if abs(det) < 1e-10:
        print("\nErro: a matriz não é invertível (determinante = 0).")
    else:
        # Resolve sistema
        X = np.linalg.solve(A, B)

         # Taxas de produção 
        x = X[0]  # Itens por trabalhador 
        y = X[1]  # Itens por máquina 
        z = X[2]  # Itens por hora 

        print("\nMatriz A:")
        for i in range(3):
            for j in range(3):
                print(f"{A[i][j]:.0f}", end=" ")
            print()

        print("\nVetor B:")
        print(B)

        print("\nTaxas de produção:")
        print(f"x = {x:.2f} itens por trabalhador")
        print(f"y = {y:.2f} itens por máquina")
        print(f"z = {z:.2f} itens por hora")

        producao = 6 * x + 3 * y + 5 * z
        print(f"\nProdução com 6 trabalhadores, 3 máquinas e 5 horas: {producao:.2f}")

        print("\nVerificação:")
        print(f"4x + 2y + 3z = {4*x + 2*y + 3*z:.2f}")
        print(f"3x + 3y + 2z = {3*x + 3*y + 2*z:.2f}")
        print(f"5x + y + 4z  = {5*x + y + 4*z:.2f}")

except np.linalg.LinAlgError:
    print("Erro: o sistema não possui solução única (matriz singular).")