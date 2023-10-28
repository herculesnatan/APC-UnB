def ler(linhas, colunas):
    sala = []
    for _ in range(linhas):
        sala.append(input().split())
    return sala

def conta_esquerda(i, fileira):
    count = 0
    if i == 0:
        return 0
    else:
        

linhas, colunas = map(int, input().split())
sala = ler(linhas, colunas)
maior = 0
for fileira in sala:
    for cadeira in range(colunas):
        if fileira[i] != "1":

        e = conta_esquerda (i, fileira)
        d = conta_direita (i, fileira)