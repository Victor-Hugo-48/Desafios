import numpy as np 

# Define a matriz dos coeficientes A e o vetor B 
A = np.array([[2, 3], [4, -1]]) 
B = np.array([8, 7]) 

# Verifica o determinante para garantir que A é invertível 
det = np.linalg.det(A) 
print(f"Determinante de A: {det:.2f}") 
 
# Calcula a inversa de A 
try: 
    A_inversa = np.linalg.inv(A) 
 
    # Calcula X = A⁻¹ * B 
    X = np.dot(A_inversa, B) 

    # Exibe a solução 
    print("\nSolução do sistema:") 
    print(f"x = {X[0]:.2f}") 
    print(f"y = {X[1]:.2f}") 

    # Verificação 
    print("\nVerificação:") 
    print(f"2x + 3y = 2({X[0]:.2f}) + 3({X[1]:.2f}) = {2*X[0] + 3*X[1]:.2f}") 
    print(f"4x - y = 4({X[0]:.2f}) - {X[1]:.2f} = {4*X[0] - X[1]:.2f}") 
except np.linalg.LinAlgError: 
    print("Erro: A matriz A é singular (não invertível).") 