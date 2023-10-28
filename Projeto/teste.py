achando  = []
resistencia = '2.70M 0.01'
fm, t = resistencia.split()
multiplicador = 'M'
fm = fm.replace('M','')
fm = float(fm)
c = fm*10**6
multiplicador = {
         '-':'Nenhuma','10**-3':'Rosa', '10**-2':'Prata','10**-1':'Dourada',  '1':'Preta',
        '10':'Marrom', '10**2':'Vermelha','10**3':'Laranja', '10**4': 'Amarela', '10**5':'Verde',
        '10**6': 'Azul',  '10**7':'Violeta','10**8':'Cinza','10**9':'Branca' 
        }
multiplicadores = {
        'm': '10**-3','-': '1', 'K':'10**3','M':'10**6','G': '10**9'
        }

for c in multiplicadores:
    if c == multiplicador:
        achando.get(multiplicador)






print(fm,c)
print(t)