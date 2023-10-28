alunos = {}
with open("alunos.txt", "r") as file:
    linha = file.readline()
    while linha:
        n, nome = linha.split()
        alunos[n] = nome
        linha = file.readline()

print(alunos)