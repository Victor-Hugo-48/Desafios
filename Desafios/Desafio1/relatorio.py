# relatorio.py
# Responsável por gerar e salvar o relatório

def gerar_relatorio(funcionarios):
    """Exibe o relatório completo no console com todos os funcionários."""
    if len(funcionarios) == 0:
        print("\nNenhum funcionário cadastrado ainda.")
        return

    print("\n" + "="*60)
    print("     RELATÓRIO DE FOLHA DE PAGAMENTO")
    print("="*60)

    total = 0.0

    for f in funcionarios:
        print(f"Nome: {f['nome']}")
        print(f"Tipo: {f['tipo']}")
        print(f"Salário Bruto:     R$ {f['bruto']:.2f}")
        print(f"Desconto INSS:     R$ {f['inss']:.2f}")
        print(f"Desconto IRRF:     R$ {f['irrf']:.2f}")
        print(f"Salário Líquido:   R$ {f['liquido']:.2f}")
        print("-" * 50)
        total += f['liquido']

    print(f"Total pago pela empresa: R$ {total:.2f}")
    print("="*60)


def salvar_relatorio(funcionarios):
    """Salva o relatório em um arquivo de texto."""
    if len(funcionarios) == 0:
        print("Nenhum funcionário para salvar.")
        return

    try:
        with open("relatorio_folha.txt", "w", encoding="utf-8") as f:
            f.write("=== Relatório de Folha de Pagamento ===\n\n")
            total = 0.0
            for func in funcionarios:
                f.write(f"Nome: {func['nome']}\n")
                f.write(f"Tipo: {func['tipo']}\n")
                f.write(f"Salário Bruto: R$ {func['bruto']:.2f}\n")
                f.write(f"Desconto INSS: R$ {func['inss']:.2f}\n")
                f.write(f"Desconto IRRF: R$ {func['irrf']:.2f}\n")
                f.write(f"Salário Líquido: R$ {func['liquido']:.2f}\n")
                f.write("-" * 40 + "\n")
                total += func['liquido']
            f.write(f"\nTotal pago pela empresa: R$ {total:.2f}\n")
        print("Relatório salvo com sucesso em 'relatorio_folha.txt'")
    except:
        print("Erro ao salvar o arquivo.")