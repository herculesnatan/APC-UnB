band = '2.70M 0.01'
#band = '1- 10'
#band = '13m 0.02'
achando = []
q = 0
v = ''

        
fm, t = band.split()
sla = ''
multi = ''
for f in fm:
    if  not f.isalpha():
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
        'm': '10**-3','-': '1', 'K':'10**3','M':'10**6','G': '10**9'
    }

Valor_Toletancia =  {
        '20':'Nenhuma', '-':'Rosa', '10':'Prata','5':'Dourada',  '-':'Preta',
        '1':'Marrom', '2%': 'Vermelha','0.05':'Laranja', '0.02':'Amarela', '0.5':'Verde',
        '0.25':'Azul', '0.1':'Violeta','0.01':'Cinza','-':'Branca'
    
        }

for x in sla:
    if x in algarismos:
        
        achei = algarismos.get(x)
        achando.append(achei)
mul = multiplicadores.get(multi)

base, exp = mul.split('**')

base = int(base)
exp = int(exp)
sla = float(sla)
a = sla * base ** exp
for i in multiplicador:
    
print(int(a))
print(achando)

