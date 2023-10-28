""""def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoof!')"""""

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:      # n é par
            n = n / 2
        else:
            n = n *3 + 1    # n é ímpar
