n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
media = input().upper()
if media == 'P':
    p1, p2, p3 = input().split()
    p1 = int(p1)
    p2 = int(p2)
    p3 = int(p3)
    calculando = (p1*n1 + p2*n2 + p3*n3)/(p1 + p2 + p3)
    print('Ponderada')
    print(f'{calculando:.2f}')
elif media == 'A':
    calculando =  (n1 + n2 + n3) /  3
    print('Aritmétrica')
    print(f'{calculando:.2f}')
elif media == 'H':
    mmc =  n1 * n2 * n3
    calculando = (3 * mmc)/ (((mmc/n1)*1) + ((mmc/n2)*1) + ((mmc/n3)*1))
    print('Harmonica')
    print(f'{calculando:.2f}')
else:
    print('Operacao inexistente')
