pessoas, ingresso = input().split()
pessoas = int(pessoas)
ingresso = int(ingresso)
valor = 0
for i in range(pessoas):
    i = int(input())
    valor += i
   
media = valor/pessoas
media = int(media)
if media >= ingresso:
    print(f'media: {media}')
    print('o rock reinara mais uma vez')
else:
    print(f'media: {media}')
    print('rockeiros trabalhando ja')
    

