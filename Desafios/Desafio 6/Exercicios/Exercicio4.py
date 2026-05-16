import numpy as np  # Importa a biblioteca NumPy

# Matriz dos coeficientes (litros de A e B)
A = np.array([
    [60, 40],  # 60L de A e 40L de B
    [50, 30]   # 50L de A e 30L de B
])

# Vetor de resultados (quantidade de ingrediente X)
B = np.array([26, 20])

# Verificar se a matriz é invertível
det = np.linalg.det(A)

if abs(det) < 1e-10:
    print("Erro: a matriz A não é invertível.")
else:
    # Resolver o sistema
    X = np.linalg.solve(A, B)

    # Guardando os valores encontrados
    x = X[0]  # unidades de X por litro de A
    y = X[1]  # unidades de X por litro de B

    # Exibição dos resultados
    print("Quantidades de ingrediente X:")
    print(f"x = {x:.2f} unidades por litro de A")
    print(f"y = {y:.2f} unidades por litro de B")

    # Cálculo para nova mistura
    unidades_x = 70 * x + 50 * y

    print("\nUnidades de X em 70L de A e 50L de B:")
    print(f"{unidades_x:.2f} unidades")

    # Verificação
    print("\nVerificação:")
    print(f"60x + 40y = {60*x + 40*y:.2f}")
    print(f"50x + 30y = {50*x + 30*y:.2f}")