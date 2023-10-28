numero = input().split()

valores = []
resultado = 0
for val in numero:
    valores.append(int(val))
qt = len(valores)

eq = valores[0]*2+valores[1]*0.5
resultado += eq
for value in valores:
    eq = value*2
    
print(resultado)



