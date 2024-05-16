nome = input()
salario = float(input())
vendas = float(input())

comissao = vendas - (vendas * 0.85)
total = comissao + salario

print("TOTAL = R$", "{:.2f}".format(total))