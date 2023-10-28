def IEC60062(resistencia: str) -> list:
    resistores = []   
    band, tol = resistencia.split()
    multiplicador = {
            '-':'Nenhuma','10**-3':'Rosa', '10**-2':'Prata','10**-1':'Dourada',  '1':'Preta',
            '10**1':'Marrom', '10**2':'Vermelha','10**3':'Laranja', '10**4': 'Amarela', '10**5':'Verde',
            '10**6': 'Azul',  '10**7':'Violeta','10**8':'Cinza','10**9':'Branca' 
            }
    multiplicadores = {
            'm': '10**-3','-': '10**0', 'K':'10**3','M':'10**6','G': '10**9'
        }
    valor_tolerancia =  {
            '20':'Nenhuma', '-':'Rosa', '10':'Prata','5':'Dourada',  '-':'Preta',
            '1':'Marrom', '2': 'Vermelha','0.05':'Laranja', '0.02':'Amarela', '0.5':'Verde',
            '0.25':'Azul', '0.1':'Violeta','0.01':'Cinza','-':'Branca'
            }
    algarismos = {
            '-':'Nenhuma',  '0':'Preta','1':'Marrom','2':'Vermelha','3':'Laranja', '4':'Amarela', '5':'Verde',
            '6':'Azul',  '7':'Violeta','8':'Cinza','9':'Branca'
            }
    for x in band:
        if x in algarismos:
            resistores.append(algarismos[x])
    if float(band) <= 10.0:
        resistores.append(algarismos.get('0'))
    mul = multiplicadores.get(band[-1])
    base, exp = mul.split('**')
    base = int(base)
    exp = int(exp)
    band = float(band)
    a = band * base ** exp
    for i in multiplicador:
        if len(i) >=2:
            base_1, exp_1 = i.split('**')
            base_1 = int(base_1)
            exp_1 = int(exp_1)
            teste = band * base_1 ** exp_1
            if teste == a:
                f = i
                mul = multiplicador.get(f)
                resistores.append(mul)        
    resistores.append(valor_tolerancia.get(tol))
    return resistores

    
    
print(IEC60062('1G 10'))
print(IEC60062('1M 10'))
print(IEC60062('2.70M 0.01'))
print(IEC60062('13m 0.02'))
print(IEC60062('2.26K 0.05'))
print(IEC60062('2.7M 1'))
print(IEC60062('2.2K 2'))
print(IEC60062('10- 20'))
print(IEC60062('10- 20'))
    