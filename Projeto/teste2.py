    for n in fm:
        if  n.isalnum():
            for x in n:
                if x.isdigit():
                    achando = algarismos.get(x)
                    resistores.append(achando)
                    
                else:
                    achando = multiplicadores.get(n)

                    if not achando in multiplicador.get(achando): 
                        if multiplicador == 'M':
                            multiplicador = '10**4'
                        resistores.append(achando)

    tole = Valor_Toletancia.get(t)
            
    resistores.append(tole)