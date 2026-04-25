# Sistema de Loja Simples - Desafio 3

##  Descrição

Este projeto foi desenvolvido como atividade acadêmica com o objetivo de simular o funcionamento de uma loja simples.
O sistema permite cadastrar produtos, realizar vendas e gerar relatórios com cálculo automático de valores.


## Funcionalidades

* Cadastro de produtos
* Listagem de produtos
* Registro de vendas
* Cálculo de valor bruto, desconto e valor final
* Geração de relatório no console
* Salvamento do relatório em arquivo `.txt`


##  Estrutura do Projeto

```
Desafio 3/
│
├── main.py
├── README.md
├── src/
    ├── __init__.py
    ├── produtos.py
    ├── vendas.py
    └── relatorio.py
├── tests/
│   ├── __init__.py
│   └── test_vendas.py


## Como executar

1. Abra o Prompt de Comando ou PowerShell

2. Acesse a pasta do projeto:
cd C:\Users\victo\OneDrive\Desktop\Desafios\Desafio3

3. Execute o programa:
python main.py


## Exemplo de saída

=== Relatório de Vendas ===

Cliente: João Silva
Produto: Camiseta
Quantidade: 15
Valor Bruto: R$ 750.00
Desconto: R$ 37.50
Valor Final: R$ 712.50

Total arrecadado pela loja: R$ 8212.50

Nome: Victor Hugo Oliveira Alves
Professor: Maxwell Gomes
Disciplina: Laboratório de Programação Competitiva 
Turma: 41