def zeroum(zeros,uns=0):
    if zeros == 0:
        # qnd zeros == 0 retorna True e termina a recurvisividade 
        print(zeros*'0'+uns*'1')
    else:
        # conta o número de zeros e concatena
        print(zeros*'0'+uns*'1')
        # diminui os zeros para fazer compração no if
        zeroum(zeros-1,uns+1)
        # printa uma nova linha de zero um
        print(zeros*'0'+uns*'1')


zeroum(5)