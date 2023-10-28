band = '2.70M'

for i in range(len(band)):
    if band[i] == '.':
        band = band.replace('.','')

print(band)