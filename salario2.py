salario_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = float(input('Horas trabalhadas: '))
salario_bruto = salario_hora * horas_trabalhadas
ir = salario_bruto * .11
inss = salario_bruto * .08
sindicato = salario_bruto * .05
desconto = (ir) + (inss) + (sindicato)
salario_liquido = (salario_bruto) - (desconto)

print(f"""
        Salário Bruto: R$ {salario_bruto}
        IR (11%): R$ {ir}
        INSS (8%): R$ {inss}
        Sindicato (5%): R$ {sindicato}
        Salário Liquido: R$ {salario_liquido}
""")