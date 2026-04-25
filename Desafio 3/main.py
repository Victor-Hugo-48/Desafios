# Arquivo principal do sistema

from src.produtos import cadastrar_produto, listar_produtos
from src.vendas import realizar_venda
from src.relatorio import gerar_relatorio, salvar_relatorio

# Listas principais do sistema
def menu():
    produtos = []
    vendas = []

    while True:
        # Exibe o menu 
        print("\n=== LOJA ===")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Realizar venda")
        print("4 - Gerar relatório")
        print("5 - Salvar relatório")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        # Controle das opções
        if opcao == "1":
            cadastrar_produto(produtos)

        elif opcao == "2":
            listar_produtos(produtos)

        elif opcao == "3":
            realizar_venda(produtos, vendas)

        elif opcao == "4":
            gerar_relatorio(vendas)

        elif opcao == "5":
            salvar_relatorio(vendas)

        elif opcao == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()