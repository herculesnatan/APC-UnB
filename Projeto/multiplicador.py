def IEC60062(resistencia): 
    # digite seu código aqui.
    resistores = []   
    fm, t = resistencia.split()
    band = ''
    multi = ''
    var = ''
    for f in fm:
        if f == '-':
            multi += f
        elif not f.isalpha():
            band += f
        else:
            multi += f
    algarismos = {
            '-':'Nenhuma',  '0':'Preta','1':'Marrom','2':'Vermelha','3':'Laranja', '4':'Amarela', '5':'Verde',
            '6':'Azul',  '7':'Violeta','8':'Cinza','9':'Branca'
            }
    multiplicador = {
            '-':'Nenhuma','10**-3':'Rosa', '10**-2':'Prata','10**-1':'Dourada',  '1':'Preta',
            '10**1':'Marrom', '10**2':'Vermelha','10**3':'Laranja', '10**4': 'Amarela', '10**5':'Verde',
            '10**6': 'Azul',  '10**7':'Violeta','10**8':'Cinza','10**9':'Branca' 
            }
    multiplicadores = {
            'm': '10**-3','-': '10**0', 'K':'10**3','M':'10**6','G': '10**9'
        }

    Valor_Toletancia =  {
            '20':'Nenhuma', '-':'Rosa', '10':'Prata','5':'Dourada',  '-':'Preta',
            '1':'Marrom', '2': 'Vermelha','0.05':'Laranja', '0.02':'Amarela', '0.5':'Verde',
            '0.25':'Azul', '0.1':'Violeta','0.01':'Cinza','-':'Branca'
            }
    for x in band:
        if x in algarismos:				# verificando se existe a band em algarismos
            achei = algarismos.get(x)
            resistores.append(achei)
            var += x
    if float(var) <= 10.0:			# condição para apenas um band
        achei = algarismos.get('0')
        resistores.append(achei)           
    mul = multiplicadores.get(multi)
    base, exp = mul.split('**')
    base = int(base)
    exp = int(exp)
    if len(band) == 1:
        caso1 = int(band) * 10
        expoente =(exp - 1 )
        base_caso, expoente_caso = base, expoente
        multi = f'{base}**{expoente_caso}'
        e = multiplicador.get(multi)
        resistores.append(e)
        resistores.append(Valor_Toletancia.get(t))
        return resistores
        
    band = float(band)
    multi_band = band * base ** exp
    var = int(var)
    for i in multiplicador:				# vendo se não existe outro multiplicador igual
        if len(i) >=2:
            base_1, exp_1 = i.split('**')
            base_1 = int(base_1)
            exp_1 = int(exp_1)
            multi_var = var * base_1 ** exp_1
            if multi_var ==  multi_band:				# comparando os valores de multi_var e  multi_band
                f = i 			# trocando se forem iguais
                mul = multiplicador.get(f)
                resistores.append(mul)        
    resistores.append(Valor_Toletancia.get(t))
    return resistores
    

print(IEC60062('1G 10'))
print(IEC60062('1- 10'))
print(IEC60062('2.70M 0.01'))
print(IEC60062('13m 0.02'))
print(IEC60062('2.26K 0.05'))
print(IEC60062('2.7M 1'))
print(IEC60062('2.2K 2'))
print(IEC60062('10- 20'))
print(IEC60062('06- 0.01'))



    


    




    