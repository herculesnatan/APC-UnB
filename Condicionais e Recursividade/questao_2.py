print("O programa funciona? ")
resposta = input().upper()

if resposta == 'SIM':
    print("Você entende o que fez? ")
    resposta = input().upper()
    if resposta == 'SIM':
        print('Ótimo. Então não mexe!')
    else:
        print('Já foi na tutoria? ')
        resposta = input().upper()
        if resposta == 'SIM':
            print('Choremos!')
        else:
            print('Temos um time a disposição!')
else:
    print('Você sabe onde está o erro? ')
    resposta = input().upper()
    if resposta == 'SIM':
        print('Acha que pode solucinar sozinho?')
        resposta = input().upper()
        if resposta == 'SIM':
            print('Então mão na massa!')
        else:
            print('Já pesquisou no Google?')
            resposta = input().upper()
            if resposta == 'SIM':
                print('Já foi na tutoria?')
                resposta = input().upper()
                if resposta == 'SIM':
                    print('Choremos!')
                else:
                    print('Temos um time a disposição!')
    else:
        print('Já foi na tutoria?')
        resposta = input().upper()
        if resposta == 'SIM':
            print('Choremos!')
        else:
            print('Temos um time a disposição!')