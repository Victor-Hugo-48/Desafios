# Módulo responsável pelo registro de vendas

def calcular_venda(produto, quantidade):
    # Calcula o valor bruto
    valor_bruto = produto["preco"] * quantidade
    
    # Regra de desconto (5% se quantidade >= 10)
    desconto = 0
    if quantidade > 10:
        desconto = valor_bruto * 0.05

    # Valor final
    valor_final = valor_bruto - desconto

    # Atualiza o estoque
    produto["estoque"] -= quantidade

    return valor_bruto, desconto, valor_final


def realizar_venda(produtos, vendas):
    # Verifica se há produtos disponíveis
    if not produtos:
        print("Sem produtos disponíveis.")
        return

    # Solicita o nome do cliente
    cliente = input("Nome do cliente: ").strip()
    if not cliente:
        print("Nome inválido!")
        return
    
    # Mostra os produtos disponíveis
    for i, p in enumerate(produtos):
        print(f"{i+1}. {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['estoque']}")

    # Escolha do produto
    try:
        escolha = int(input("Escolha o produto: ")) - 1
        produto = produtos[escolha]
    except:
        print("Escolha inválida!")
        return

    # Quantidade
    try:
        quantidade = int(input("Quantidade: "))
    except:
        print("Quantidade inválida!")
        return

    # Verificação de estoque
    if quantidade <= 0 or quantidade > produto["estoque"]:
        print("Estoque insuficiente!")
        return
    
    # Cálculo da venda (função separada)
    valor_bruto, desconto, valor_final = calcular_venda(produto, quantidade)

    # Registro da venda
    vendas.append({
        "cliente": cliente,
        "produto": produto["nome"],
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final
    })

    print("Venda realizada com sucesso!")