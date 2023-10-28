# criando a equação ax^2 + bx + c
def raizes(a,b,c):
    # calculando bhaskara
    delta = (b**2) - (4 * a * c)
    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    else:
        return -1

print(raizes(6,11,-35)) 
print(raizes(2,4,2))
print(raizes(-4,-7,-12))
