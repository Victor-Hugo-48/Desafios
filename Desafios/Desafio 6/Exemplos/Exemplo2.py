import numpy as np 

# Define a matriz dos coeficientes A e o vetor B 
A = np.array([[2, 1, 2], [1, 2, 3], [3, 1, 4]]) 
B = np.array([7, 7, 11]) 

# Verifica o determinante para garantir que A é invertível 
det = np.linalg.det(A) 
print(f"Determinante de A: {det:.2f}") 

# Resolve o sistema diretamente 
try: 
    X = np.linalg.solve(A, B) 

    # Taxas de produção 
    x = X[0]  # Itens por trabalhador 
    y = X[1]  # Itens por máquina 
    z = X[2]  # Itens por hora 

    # Exibe a solução 
    print("\nTaxas de produção:") 
    print(f"x = {x:.2f} itens por trabalhador") 
    print(f"y = {y:.2f} itens por máquina") 
    print(f"z = {z:.2f} itens por hora")

# Calcula produção com 4 trabalhadores, 2 máquinas e 3 horas 
    producao = 4 * x + 2 * y + 3 * z 
    print(f"\nProdução com 4 trabalhadores, 2 máquinas e 3 horas: {producao:.2f} itens") 

    # Verificação 
    print("\nVerificação:") 
    print(f"2x + y + 2z = 2({x:.2f}) + {y:.2f} + 2({z:.2f}) = {2*x + y + 2*z:.2f}") 
    print(f"x + 2y + 3z = {x:.2f} + 2({y:.2f}) + 3({z:.2f}) = {x + 2*y + 3*z:.2f}") 
    print(f"3x + y + 4z = 3({x:.2f}) + {y:.2f} + 4({z:.2f}) = {3*x + y + 4*z:.2f}") 
except np.linalg.LinAlgError: 
    print("Erro: A matriz A é singular (não invertível).") 