def IEC60062(resistencia):
    resistores = []   
    valor, tolerancia = resistencia.split()
    multiplicador = valor[-1]
    valor = (valor[:-1])
    

    algarismos = {
        '-':'Nenhuma', '0':'Preta', '1':'Marrom','2':'Vermelha','3':'Laranja', '4':'Amarela', '5':'Verde',
        '6':'Azul',  '7':'Violeta','8':'Cinza','9':'Branca'
    }
    multiplicadores = {
        '-':'Nenhuma','10**-3':'Rosa', '10**-2':'Prata','10**-1':'Dourada',  '10**-1':'Preta',
        '10**1':'Marrom', '10**2':'Vermelha','10**3':'Laranja', '10**4': 'Amarela', '10**5':'Verde',
        '10**6': 'Azul',  '10**7':'Violeta','10**8':'Cinza','10**9':'Branca' 
    }
    multiplicadores = {
            'm': '10**-3','-': '10**0', 'K':'10**3','M':'10**6','G': '10**9'
        }

    tolerancias = {
        '20':'Nenhuma', '10':'Prata','5':'Dourada', '1':'Marrom', '2': 'Vermelha','0.05':'Laranja', '0.02':'Amarela', '0.5':'Verde',
        '0.25':'Azul', '0.1':'Violeta','0.01':'Cinza'
    }
    
    valor_string = str(valor)
    for i in range(len(valor_string)):
        if valor_string[i] != '.':
            resistores.append(algarismos[valor_string[i]])
    resistores.append(multiplicadores[multiplicador])
    valor = float(valor)
    if multiplicador == 'm':
        multiplicando = valor * 10 ** -3
    elif multiplicador == 'K':
        multiplicando = valor * 10 ** 3
    elif multiplicador == 'M':
        multiplicando = valor * 10 ** 6
    elif multiplicador == 'G':
        multiplicando = valor * 10 ** 9
    
    resistores.append(tolerancias[tolerancia])
    return resistores





print(IEC60062('2.70M 0.01'))