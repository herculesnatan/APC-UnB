import math as m
def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    raiz = (dx**2) + (dy**2)
    resultado = m.sqrt(raiz)
    return resultado

print(distancia(0,0,10,10))