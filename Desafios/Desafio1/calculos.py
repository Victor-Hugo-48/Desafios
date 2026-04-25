# calculos.py
# Arquivo responsável por todos os cálculos de salário

def calcular_salario_estagiario(salario_fixo):
    """Calcula o salário do estagiário.
    Estagiário não tem nenhum desconto (INSS ou IRRF)."""
    if salario_fixo <= 0:
        raise ValueError("Salário fixo deve ser maior que zero.")
    
    return salario_fixo, 0.0, 0.0, salario_fixo  # bruto, inss, irrf, liquido


def calcular_salario_clt(salario_bruto):
    """Calcula o salário do funcionário CLT.
    - Desconto fixo de 8% para INSS
    - Desconto de 10% para IRRF apenas se salário > R$ 2000"""
    if salario_bruto <= 0:
        raise ValueError("Salário bruto deve ser maior que zero.")
    
    inss = round(salario_bruto * 0.08, 2)
    irrf = round(salario_bruto * 0.10, 2) if salario_bruto > 2000 else 0.0
    liquido = round(salario_bruto - inss - irrf, 2)
    
    return salario_bruto, inss, irrf, liquido


def calcular_salario_freelancer(horas, valor_hora):
    """Calcula o salário do freelancer.
    Recebe por hora trabalhada e tem desconto fixo de 5%."""
    if horas <= 0 or valor_hora <= 0:
        raise ValueError("Horas e valor por hora devem ser maiores que zero.")
    
    bruto = round(horas * valor_hora, 2)
    desconto = round(bruto * 0.05, 2)
    liquido = round(bruto - desconto, 2)
    
    return bruto, desconto, 0.0, liquido