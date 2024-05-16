A, B, C = map(float, input().split())

# A) A área do triângulo retângulo que tem A por base e C por altura.

areaTriangulo = 1/2 * A * C
print(f"TRIANGULO: {areaTriangulo:.3f}")

# B) A área do cículo de raio C. (pi = 3.14159)

pi = 3.14159
areaCirculo = pi * C ** 2
print(f"CIRCULO: {areaCirculo:.3f}")

# C) A área do trapézio que tem A e B por bases e C por altura.

areaTrapezio = 1/2 * (A + B) * C
print(f"TRAPEZIO: {areaTrapezio:.3f}")

# D) A área do quadrado que tem lado B.

areaQuadrado = B * B
print(f"QUADRADO: {areaQuadrado:.3f}")

# E) A área do retângulo que tem lados A e B.

areaRetangulo = A * B
print(f"RETANGULO: {areaRetangulo:.3f}")