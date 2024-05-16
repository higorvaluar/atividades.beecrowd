valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)

for nota in notas:
    quantidade_notas = valor // nota
    valor %= nota
    print(f"{quantidade_notas} nota(s) de R$ {nota},00")