# Desafio  DESAFIO 5 - GERAR MATRIZ COM NÚMEROS ALEATÓRIOS

## Informações do Aluno
- **Nome:** Victor Hugo Oliveira Alves
- **Professor:** Maxwell Gomes
- **Disciplina:** LABORATÓRIO DE PROGRAMAÇÃO COMPETITIVA  
- **Curso:** Sistemas de Informação


## Descrição do Projeto
Este projeto tem como objetivo demonstrar a criação e manipulação de matrizes em Python utilizando duas abordagens:
1. **Biblioteca `random`** → construção manual da matriz com estruturas de repetição  
2. **Biblioteca `NumPy`** → geração automática de matrizes de forma otimizada  


## Tecnologias Utilizadas
- Python 3  
- Biblioteca `random` (nativa)  
- Biblioteca `numpy`  

## Funcionamento
Método 1 - Random
- Cria uma matriz vazia
- Usa laços `for` para preencher linha por linha
- Gera números aleatórios com `random.randint()`

Método 2 - NumPy
- Utiliza `np.random.randint()`
- Gera a matriz completa em uma única linha
- Mais rápido e eficiente

## Como Executar
1. Instale o Python (caso não tenha)
2. Instale o NumPy:
   ```bash
   pip install numpy