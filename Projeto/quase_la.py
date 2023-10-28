def IEC60062(resistencia):

    algarismos = {
        '-':'Nenhuma', '0':'Preta', '1':'Marrom','2':'Vermelha','3':'Laranja', '4':'Amarela', '5':'Verde',
        '6':'Azul',  '7':'Violeta','8':'Cinza','9':'Branca'
    }
    
    multiplicador_cor = {
        '-':'Nenhuma','10**-3':'Rosa', '10**-2':'Prata','10**-1':'Dourada',  '10**0':'Preta',
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
    
    resistores = []
    var = ''
    valor, tolerancia = resistencia.split()
    multiplicador = valor[-1]
    valor = (valor[:-1])
    valor_string = str(valor)
    for i in range(len(valor_string)):
        if valor_string[i] != '.':
            resistores.append(algarismos[valor_string[i]])
            var  += valor_string[i]
    if float(var) <= 10.0: 
        achei = algarismos.get('0')
        resistores.append(achei)
    mul = multiplicadores.get(multiplicador)
    base,exp = mul.split('**')
    base, exp = int(base),int(exp)
    if len(valor_string) == 1:
        caso = int(valor_string) * 10
        expoente = (exp - 1)
        multi = f'{base}**{expoente}'
        expo_caso = multiplicador_cor.get(multi)
        resistores.append(expo_caso)
        resistores.append(tolerancias.get(tolerancia))
        return resistores
    multi_band = float(valor) * base ** exp
    var = int(var)
    for i in multiplicador_cor:
        if len (i) >= 2:
            base_1, exp_1 = i.split('**')
            base_1,exp_1 = int(base_1),int(exp_1)
            multi_var = var * base_1 ** exp_1
            if multi_var ==  multi_band:				# comparando os valores de multi_var e  multi_band
                valor_multi = i 			# trocando se forem iguais
                mul = multiplicador_cor.get(valor_multi)
                resistores.append(mul)        
    resistores.append(tolerancias.get(tolerancia))
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


'''
['Marrom', 'Preta', 'Cinza', 'Prata']
['Marrom', 'Preta', 'Dourada', 'Prata']
['Vermelha', 'Violeta', 'Preta', 'Azul', 'Cinza']
['Marrom', 'Laranja', 'Rosa', 'Amarela']
['Vermelha', 'Vermelha', 'Azul', 'Laranja', 'Laranja']
['Vermelha', 'Violeta', 'Azul', 'Marrom']
['Vermelha', 'Vermelha', 'Laranja', 'Vermelha']
['Marrom', 'Preta', 'Preta', 'Preta', 'Nenhuma']
['Preta', 'Azul', 'Preta', 'Preta', 'Cinza']

'''


    