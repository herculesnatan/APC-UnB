frase = input()
if 'zero' in frase:
    nova_frase = frase.replace('zero','0')
elif 'um' in frase:
    nova_frase = frase.replace('um', '1')
elif 'dois' in frase:
    nova_frase = frase.replace('dois', '2')
elif 'três' in frase:
    nova_frase = frase.replace('três', '3')
elif 'quatro' in frase:
    nova_frase = frase.replace('quatro', '4')
elif 'cinco' in frase:
    nova_frase = frase.replace('cinco', '5')
elif 'seis' in frase:
    nova_frase = frase.replace('seis', '6')
elif 'sete' in frase:
    nova_frase = frase.replace('sete', '7')
elif 'oito' in frase:
    nova_frase = frase.replace('oito', '8')
elif 'nove' in frase:
    nova_frase = frase.replace('nove', '9')
else:
    nova_frase = frase.replace('zeroum', '01')


print(nova_frase)