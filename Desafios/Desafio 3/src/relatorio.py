# Módulo responsável pela geração de relatórios

def gerar_relatorio(vendas):
    # Verifica se existem vendas
    if not vendas:
        print("Nenhuma venda realizada.")
        return

    total = 0

    # Título do relatório
    print("\n=== Relatório de Vendas ===")

# Percorre todas as vendas
    for v in vendas:
        print(f"\nCliente: {v['cliente']}")
        print(f"Produto: {v['produto']}")
        print(f"Quantidade: {v['quantidade']}")
        print(f"Valor Bruto: R$ {v['valor_bruto']:.2f}")
        print(f"Desconto: R$ {v['desconto']:.2f}")
        print(f"Valor Final: R$ {v['valor_final']:.2f}")

 # Soma o total arrecadado
        total += v["valor_final"]

 # Exibe o total final
    print(f"\nTotal arrecadado pela loja: R$ {total:.2f}")


def salvar_relatorio(vendas):
    try:
        # Abre (ou cria) o arquivo de relatório
        with open("relatorio_vendas.txt", "w", encoding="utf-8") as f:
            total = 0

            f.write("=== Relatório de Vendas ===\n")

# Escreve cada venda no arquivo
            for v in vendas:
                f.write(f"\nCliente: {v['cliente']}\n")
                f.write(f"Produto: {v['produto']}\n")
                f.write(f"Quantidade: {v['quantidade']}\n")
                f.write(f"Valor Bruto: R$ {v['valor_bruto']:.2f}\n")
                f.write(f"Desconto: R$ {v['desconto']:.2f}\n")
                f.write(f"Valor Final: R$ {v['valor_final']:.2f}\n")

                total += v["valor_final"]

# Escreve o total final
            f.write(f"\nTotal arrecadado pela loja: R$ {total:.2f}")

        print("Relatório salvo com sucesso!")

    except:
        print("Erro ao salvar o relatório.")