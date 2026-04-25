# Desafio 2 sobre Listas em Python

def executar_main():
    # Criando listas
    print("===  # Criando listas ===")
    frutas = ["maçã", "banana", "laranja"]
    numeros = [1, 2, 3, 4, 5]
    misturado = [1, "texto", 3.14, True]
    print("Lista de frutas:", frutas)
    print("Lista de números:", numeros)

    # Acessando elementos
    print("\n=== Acessando elementos ===")
    print("Primeira fruta (índice 0):", frutas[0])    # retorna "maçã"
    print("Última fruta (índice -1):", frutas[-1])   # retorna "laranja"
    print("Sublista (fatiamento 1:3):", numeros[1:4]) # retorna [2, 3, 4]

    # Iteração sobre listas
    print("\n=== Iteração sobre listas ===")
    print("Usando for:")
    for fruta in frutas:
        print(f"Fruta: {fruta}")

    print("\nUsando while:")
    indice = 0
    while indice < len(frutas):
        print(f"Fruta no índice {indice}: {frutas[indice]}")
        indice += 1

    # Operações com listas
    print("\n===  Operações com listas ===")
    frutas.append("morango")  # Adiciona ao final
    print("Após append('morango'):", frutas)

    frutas.remove("banana")   # Remove por valor
    print("Após remove('banana'):", frutas)

    frutas[1] = "kiwi"        # Modifica elemento
    print("Após modificar índice 1 para 'kiwi':", frutas)

    nova_lista = frutas + ["uva", "manga"] # Concatena
    print("Após concatenar com nova lista:", nova_lista)
   
   # Empilhamento (pilhas)
    print("\n=== Empilhamento (pilhas LIFO) ===")
    pilha = []
    pilha.append(1) # Empilha 1
    pilha.append(2) # Empilha 2
    pilha.append(3) # Empilha 3
    print("Pilha após empilhar (1, 2, 3):", pilha)

    ultimo = pilha.pop() # Remove e retorna o último elemento
    print("Elemento desempilhado (pop):", ultimo)
    print("Pilha após desempilhar:", pilha)

    # Outras operações
    print("\n=== Outras operações ===")
    numeros_desordenados = [5, 2, 8, 1, 9]
    print("Tamanho da lista (len):", len(numeros_desordenados))
    print("O número 8 está na lista? (in):", 8 in numeros_desordenados)
    
    numeros_desordenados.sort()
    print("Lista ordenada (sort):", numeros_desordenados)
    
    numeros_desordenados.reverse()
    print("Lista invertida (reverse):", numeros_desordenados)

    # Listas aninhadas
    print("\n=== Listas aninhadas ===")
    matriz = [[1, 2], [3, 4]]
    print("Matriz completa:", matriz)
    print("Acessando elemento matriz[0][1]:", matriz[0][1]) # acessa o 2

    # Compreensão de listas
    print("\n=== Compreensão de listas ===")
    quadrados = [x**2 for x in range(1, 6)]
    print("Quadrados de 1 a 5:", quadrados)


# Bloco de execução principal
if __name__ == "__main__":
    executar_main()