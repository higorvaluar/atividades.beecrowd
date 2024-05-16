A, B, C = map(float, input().split())

delta = B**2 - 4*A*C

if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    rdelta = delta ** 0.5
    x1 = (-B + rdelta) / (2*A)
    x2 = (-B - rdelta) / (2*A)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")