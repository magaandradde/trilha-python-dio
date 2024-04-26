salario = 2000  # escopo global


def salario_bonus(bonus):
    global salario  # se você não informar que esse objeto é global dá erro na saída
    salario += bonus
    return salario


novo_salario = salario_bonus(500)  # 2500
print(novo_salario)