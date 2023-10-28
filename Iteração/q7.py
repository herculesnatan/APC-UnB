def IEC60062(resistencia):
    # digite seu código aqui.
    resistores = []
    fm, t = resistencia.split()
    algarismos = {
         '-':'Nenhuma', '-':'Rosa', '-':'Prata','-':'Dourada',  '0':'Preta',
        '1':'Marrom','2':'Vermelha','3':'Laranja', '4':'Amarela', '5':'Verde',
        '6':'Azul',  '7':'Violeta','8':'Cinza','9':'Branca'
        }
    multiplicador = {
         '-':'Nenhuma','10**-3':'Rosa', '10**-2':'Prata','10**-1':'Dourada',  '1':'Preta',
        '10':'Marrom', '10**2':'Vermelha','10**3':'Laranja', '10**4': 'Amarela', '10**5':'Verde',
        '10**6': 'Azul',  '10**7':'Violeta','10**8':'Cinza','10**9':'Branca' 
        }
    multiplicadores = {
        'm': '10**-3','-': '1', 'K':'10**3','M':'10**6','G': '10**9'
    }
    Valor_Toletancia =  {
        '20':'Nenhuma', '-':'Rosa', '10':'Prata','5':'Dourada',  '-':'Preta',
        '1':'Marrom', '2%': 'Vermelha','0.05':'Laranja', '0.02':'Amarela', '0.5':'Verde',
        '0.25':'Azul', '0.1':'Violeta','0.01':'Cinza','-':'Branca'
    
        }
    
    for n in fm:
        if  n.isalnum():
            for x in n:
                if x.isdigit():
                    achando = algarismos.get(x)
                    resistores.append(achando)
                else:
                    achando = multiplicadores.get(x)
                    if not achando in multiplicador.get(achando): 
                        if not multiplicador == 'M':
                            multiplicador = '10**4'
                        resistores.append(achando)
    

        tole = Valor_Toletancia.get(t)
            
    resistores.append(tole)
    return resistores
    
    

print(IEC60062('2.70M 0.01'))
print(IEC60062('1- 10'))
print(IEC60062('13m 0.02'))