n = int(input())
pessoas = []
for i in range(n):
    pessoas.append(input())
foras = input().split()
saida = []
for pessoa in pessoas:
    if not pessoa in foras:
        saida.append(pessoa)

print(' '.join(saida))



