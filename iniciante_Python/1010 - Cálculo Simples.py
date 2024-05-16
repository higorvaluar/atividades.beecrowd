cP1, nP1, vU1 = map(float, input().split())
cP2, nP2, vU2 = map(float, input().split())

total = (nP1 * vU1) + (nP2 * vU2)

print(f"VALOR A PAGAR: R$ {total:.2f}")