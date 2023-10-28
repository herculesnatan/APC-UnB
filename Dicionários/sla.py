def ligados(p1,p2):
    for key, value in pessoas.items():
        if value == p2:
            key = p2
            break
    return p2 in ass[p1]
p,a,q = map(int,input().split())
pessoas = {}
ass = {}
for _ in range(p):
    linha = input().split()
    pessoas[linha[0]] = linha [1]
for _ in range(a):
    linha = input().split()
    ass[linha[0]] =  linha[1:]

for _ in range(q):
    pessoa_1, pessoa_2 = input().split()
    if ligados(pessoa_1, pessoa_2):
        print('Sim')
    else:
        print('Não')
