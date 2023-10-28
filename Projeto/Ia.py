def IEC60062(resistencia):
    resistores = []   
    valor, tolerancia = resistencia.split()
    multiplicador = valor[-1]
    valor = float(valor[:-1])
    if multiplicador == 'm':
        valor = valor * 10 ** -3
    elif multiplicador == 'K':
        valor = valor * 10 ** 3
    elif multiplicador == 'M':
        valor = valor * 10 ** 6
    elif multiplicador == 'G':
        valor = valor * 10 ** 9

    algarismos = {
        '-':'Nenhuma', '0':'Preta', '1':'Marrom','2':'Vermelha','3':'Laranja', '4':'Amarela', '5':'Verde',
        '6':'Azul',  '7':'Violeta','8':'Cinza','9':'Branca'
    }
    multiplicadores = {
        '-':'Nenhuma','10**-3':'Rosa', '10**-2':'Prata','10**-1':'Dourada',  '1':'Preta',
        '10**1':'Marrom', '10**2':'Vermelha','10**3':'Laranja', '10**4': 'Amarela', '10**5':'Verde',
        '10**6': 'Azul',  '10**7':'Violeta','10**8':'Cinza','10**9':'Branca' 
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
    resistores.append(tolerancias[tolerancia])
    return resistores

#print(IEC60062('1G 10'))
#print(IEC60062('1M 10'))
print(IEC60062('2.70M 0.01'))
#print(IEC60062('13m 0.02'))
#print(IEC60062('2.26K 0.05'))
#print(IEC60062('2.7M 1'))
