caracter = input()
inverter = caracter[::-1]

frase = input()

while frase != '':
    frase = frase.replace(caracter,'')
    frase = frase.replace(inverter,'')
    print(frase)
    frase = input()
