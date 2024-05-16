N = int(input())

horas = N // 3600
sRestante = N % 3600
minutos = sRestante // 60
segundosFinais = sRestante % 60

print(f"{horas}:{minutos}:{segundosFinais}")