def paron(lista):
    #comece aqui
    vogais = ["a","e","i","o","u"]
    final = []
    for palavra in lista:
        count = 0
        for c in palavra:
            if c in vogais or c.lower() in vogais:
                count += 1
        if count % 2 == 0:
            final.append(palavra)
    return final
print(paron(['todos', 'nos', 'adoramos', 'disciplina', 'apc']))
