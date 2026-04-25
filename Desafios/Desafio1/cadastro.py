# cadastro.py
# Responsável pelo cadastro de novos funcionários com validações

from calculos import calcular_salario_estagiario, calcular_salario_clt, calcular_salario_freelancer

def cadastrar_funcionario():
    """Solicita os dados do funcionário, valida e retorna um dicionário."""
    nome = input("\nNome do funcionário: ").strip()
    if not nome:
        print("Erro: Nome não pode ser vazio.")
        return None

    tipo = input("Tipo (estagiario / clt / freelancer): ").strip().lower()

    if tipo not in ["estagiario", "clt", "freelancer"]:
        print("Erro: Tipo inválido.")
        return None

    try:
        if tipo == "estagiario":
            salario = float(input("Salário fixo (R$): "))
            bruto, inss, irrf, liquido = calcular_salario_estagiario(salario)
            tipo_nome = "Estagiário"

        elif tipo == "clt":
            salario = float(input("Salário bruto (R$): "))
            bruto, inss, irrf, liquido = calcular_salario_clt(salario)
            tipo_nome = "CLT"

        else:  # freelancer
            horas = float(input("Horas trabalhadas: "))
            valor_hora = float(input("Valor por hora (R$): "))
            bruto, inss, irrf, liquido = calcular_salario_freelancer(horas, valor_hora)
            tipo_nome = "Freelancer"

        return {
            "nome": nome,
            "tipo": tipo_nome,
            "bruto": bruto,
            "inss": inss,
            "irrf": irrf,
            "liquido": liquido
        }

    except ValueError:
        print("Erro: Digite apenas números válidos.")
        return None