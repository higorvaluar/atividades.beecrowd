nFuncionario = int(input())
hTrabalhadas = int(input())
vHoras = float(input())

SALARIO = hTrabalhadas * vHoras

print("NUMBER =", nFuncionario)
print("SALARY = U$", "{:.2f}".format(SALARIO))