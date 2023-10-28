n_pessoas = int(input())
pessoas = []
for value in range(n_pessoas):
    value = input()
    pessoas.append(value)

pessoas.sort(reverse=True)

for pessoa in pessoas:
    print(pessoa)