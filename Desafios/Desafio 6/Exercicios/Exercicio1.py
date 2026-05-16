import numpy as np # Importa a NumPy

# Matriz dos coeficientes
A = np.array([[5, 3], [8, 2]])

# Vetor de resultados
B = np.array([110, 100])

# Resolvendo o sistema
X = np.linalg.solve(A, B)

# Pegando os valores
x = X[0] # Itens por trabalhador
y = X[1] # Itens por máquina 

print("Taxas de produção:")
print(f"x = {x:.2f} itens por trabalhador por dia")
print(f"y = {y:.2f} itens por máquina por dia")

# Nova produção com 10 trabalhadores e 4 máquinas
producao = 10 * x + 4 * y
print(f"\nProdução com 10 trabalhadores e 4 máquinas: {producao:.2f} itens")

# Verificação
print("\nVerificação:")
print(f"5x + 3y = {5*x + 3*y:.2f}")
print(f"8x + 2y = {8*x + 2*y:.2f}")