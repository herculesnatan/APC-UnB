import random
cont = 0
jogo = random.randint(1, 61)
while cont < 7:
    cont += 1
    print(jogo,end=' ')
    jogo = random.randint(1, 61)