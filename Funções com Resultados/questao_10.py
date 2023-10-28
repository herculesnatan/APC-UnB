def mdc(valor1, valor2):
    # calculando mdc
    while valor2 != 0:
        resto = valor1 % valor2
        valor1 =  valor2
        valor2 = resto

    return valor1
print(mdc(12,30))
