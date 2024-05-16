X = int(input())
def um_decimal(Y):
    return round(Y, 1)
Y = float(input())
Y = um_decimal(Y)

KML = X / Y

print(f"{KML:.3f} km/l")