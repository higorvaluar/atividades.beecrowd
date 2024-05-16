A, B, C = map(int, input().split())

MaiorAB = (A + B + abs(A - B)) // 2

maior = (MaiorAB + C + abs(MaiorAB - C)) // 2

print(int(maior), "eh o maior")