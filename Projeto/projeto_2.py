a = '2.70M 0.01'
fm, t = a.split()
resistores = []
Algarismo_significativo = {
    '—': 'Nenhuma', '—': 'Rosa', '—': 'Prata', '—':'Dourada', '0':'Preta',
    '1':'Marrom', '2':'Vermelha', '3': 'Laranja', '4':'Amarela', '5':'Verde',
    '6': 'Azul', '7':'Violeta', '8':'Cinza', '9': 'Branca'
}

multiplicador = {
         '—':'Nenhuma',10**-3:'Rosa', 10**-2:'Prata',10**-1:'Dourada',  1:'Preta',
        10:'Marrom', 10**2:'Vermelha',10**3:'Laranja', 10**4: 'Amarela', 10**5:'Verde',
        10**6: 'Azul',  10**7:'Violeta',10**8:'Cinza',10**9:'Branca' 
        }

multiplicadores = {
        10**-3: 'm', 1: '—',10**3: 'K',10**6: 'M',10**9: 'G'
    }
Valor_Toletancia =  {
        '20':'Nenhuma', '—':'Rosa', '10':'Prata','5':'Dourada',  '—':'Preta',
        '1':'Marrom', '2%': 'Vermelha','0.05':'Laranja', '002':'Amarela', '0.5':'Verde',
        '0.25':'Azul', '0.1':'Violeta','001':'Cinza','—':'Branca'
    
        }
for char in fm:
    if char.isalpha():
        fm = fm.replace(char,'')
for n in fm:

    achando = Algarismo_significativo.get(n)
    resistores.append(achando)                
    
    achando = multiplicadores.get(char)

    resistores.append(achando)

    tole = Valor_Toletancia.get(t)
            
    resistores.append(tole)
print(resistores)


    