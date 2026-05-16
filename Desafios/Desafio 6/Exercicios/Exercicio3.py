import numpy as np  # Biblioteca para cálculos matemáticos

# Matriz dos coeficientes (pães e bolos)
A = np.array([
    [50, 20],  # 50 pães e 20 bolos
    [30, 30]   # 30 pães e 30 bolos
])

# Vetor de resultados (quantidade total)
B = np.array([30, 12])  # farinha e açúcar

# Verificar se a matriz é invertível
det = np.linalg.det(A)

if abs(det) < 1e-10:
    print("Erro: a matriz não é invertível.")
else:
    # Resolver o sistema
    X = np.linalg.solve(A, B)

    # Guardando os valores
    x = X[0]  # farinha por pão
    y = X[1]  # açúcar por bolo

    # Mostrar resultados
    print("Quantidades por unidade:")
    print(f"x = {x:.2f} kg de farinha por pão")
    print(f"y = {y:.2f} kg de açúcar por bolo")

    # Calcular consumo
    farinha = 40 * x + 25 * y
    acucar = 40 * x + 25 * y

    print("\nConsumo para 40 pães e 25 bolos:")
    print(f"Farinha: {farinha:.2f} kg")
    print(f"Açúcar: {acucar:.2f} kg")

    # Verificação
    print("\nVerificação:")
    print(f"50x + 20y = {50*x + 20*y:.2f}")
    print(f"30x + 30y = {30*x + 30*y:.2f}")