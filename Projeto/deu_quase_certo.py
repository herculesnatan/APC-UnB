def IEC60062(resistencia):
    # digite seu código aqui.
    resistores = []   
    fm, t = resistencia.split()
    sla = ''
    multi = ''
    var = ''
    for f in fm:
        if f == '-':
            multi += f
        elif not f.isalpha():
            sla += f
        else:
            multi += f
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
            'm': '10**-3','-': '10**0', 'K':'10**3','M':'10**6','G': '10**9'
        }

    Valor_Toletancia =  {
            '20':'Nenhuma', '-':'Rosa', '10':'Prata','5':'Dourada',  '-':'Preta',
            '1':'Marrom', '2': 'Vermelha','0.05':'Laranja', '0.02':'Amarela', '0.5':'Verde',
            '0.25':'Azul', '0.1':'Violeta','0.01':'Cinza','-':'Branca'
        
            }
    mul = multiplicadores.get(multi)
    base, exp = mul.split('**')
    base = int(base)
    exp = int(exp)
    for x in sla:
        if len(sla) < 2:
                caso1 = int(sla) * 10
                multi = '10**-1'
                resistores.append(achei)
                e = multiplicador.get(multi)
                resistores.append(e)
            if x in algarismos:
                achei = algarismos.get(x)
                resistores.append(achei)
            
                
            var += x
            
    
    

        
    sla = float(sla)
    a = sla * base ** exp
    a = float(a)
    var = int(var)
    for i in multiplicador:
        if len(i) >=3:
            base_1, exp_1 = i.split('**')
            base_1 = int(base_1)
            exp_1 = int(exp_1)
            teste = var * base_1 ** exp_1
            if teste == a:
                f = i
                mul = multiplicador.get(f)
                resistores.append(mul)
                
    resistores.append(Valor_Toletancia.get(t))
    
    return resistores
    

#print(IEC60062('2.70M 0.01'))

print(IEC60062('1- 10'))

#print(IEC60062('13m 0.02'))
            


    


    


