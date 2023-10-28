#Escreva um programa que leia três números distintos e os imprima em
#ordem decrescente.

a, b, c = map(int,input().split())
# a maior que todos 
if a > b and a > c:
    if b > c:
        print(a,b,c)
    else:
        print(a,c,b)
# b maior que todos
elif b > a and b > c:
    if a > c:
        print(b,a,c)
    else:
        print(b,c,a)
else:
    if b > a:
        print(c,b,a)
    else:
        print(c,a,b)