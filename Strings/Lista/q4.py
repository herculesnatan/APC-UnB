frase = input()
frase_final = ''

for char in range(len(frase)):
    if char % 2 == 0:
        continue
    else:
        frase_final += frase[char]
    
print(frase_final.replace(' ',''))

    


