def dois_decimais(monetario):
    return round(monetario, 2)

monetario = float(input())
monetario = dois_decimais(monetario)

centavos = int(monetario * 100)

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    quantidade_notas = centavos // nota
    centavos %= nota
    if nota >= 100:
        print(f"{quantidade_notas} nota(s) de R$ {nota / 100:.2f}")

print("MOEDAS:")
for moeda in moedas:
    quantidade_moedas = centavos // moeda
    centavos %= moeda
    print(f"{quantidade_moedas} moeda(s) de R$ {moeda / 100:.2f}")