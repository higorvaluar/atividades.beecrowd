dias = int(input())

anos = dias // 365
diasRestantes = dias % 365
mes = diasRestantes // 30

print(f"{anos} ano(s)")
print(f"{mes} mes(es)")
print(f"{diasRestantes % 30} dia(s)")