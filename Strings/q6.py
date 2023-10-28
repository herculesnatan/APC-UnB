frase = input()
palavra = input()

if palavra in frase:
    nova_frase = frase.replace(palavra,'*')
    print(nova_frase)
else:
    print('tudo certo :)')