from math import sqrt 
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

distancia = ((x1 + y1) - (x2+y2))**2
distancia = sqrt(distancia)
print(distancia)


if distancia <= 100:
    print("É o amor da minha vida!")

elif distancia <= 200:
    print('Talvez dê certo')

else:
    print('Não vale a pena investir')
