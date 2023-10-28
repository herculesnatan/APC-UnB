frase = input()
lag = True
cont = 0

for x in frase:
    if x.isnumeric():
        cont +=1
    
print(cont)