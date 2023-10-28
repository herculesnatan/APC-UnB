n = input().split()
valores = []
multiplos = []
for val in n:
    valores.append(int(val))
num = int(input())

for numeros in valores:
    if numeros % num == 0:
        multiplos.append(int(numeros))

for resultado in multiplos:
    print(resultado,end=' ')