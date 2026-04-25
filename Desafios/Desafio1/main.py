# main.py - Menu principal do sistema

from cadastro import cadastrar_funcionario
from relatorio import gerar_relatorio, salvar_relatorio

def main():
    """Função principal que controla o menu do programa."""
    funcionarios = []

    print("=== Sistema de Folha de Pagamento ===\n")

    while True:
        print("1 - Cadastrar funcionário")
        print("2 - Gerar relatório")
        print("3 - Salvar relatório em arquivo")
        print("4 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            novo = cadastrar_funcionario()
            if novo:
                funcionarios.append(novo)
                print("Funcionário cadastrado com sucesso!\n")

        elif opcao == "2":
            gerar_relatorio(funcionarios)

        elif opcao == "3":
            salvar_relatorio(funcionarios)

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    main()