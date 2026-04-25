# Módulo responsável pelo gerenciamento de produtos

def cadastrar_produto(produtos):
    # Solicita o nome e o preço do produto
    nome = input("Nome do produto: ").strip().lower()

    if not nome:
        print("Nome inválido!")
        return

    for p in produtos:
        if p["nome"] == nome:
            print("Produto já existe!")
            return

    try:
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
    except:
        print("Entrada inválida!")
        return

    if preco <= 0 or estoque < 0:
        print("Valores inválidos!")
        return

  # Adiciona o produto na lista como um dicionário
    produtos.append({
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    })
 # Confirmação para o usuário
    print("Produto cadastrado com sucesso!")


def listar_produtos(produtos):
    # Verifica se existem produtos cadastrados
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

# Exibe todos os produtos cadastrados
    for i, p in enumerate(produtos):
        print(f"{i+1}. {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['estoque']}")