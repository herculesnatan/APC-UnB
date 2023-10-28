def ehprimo(num):
    count = 0
    for i in range(2, num):
        if (num % i == 0):
            count += 1
    if count == 0:
        return 1
    else:
        return 0
    


def divisoresPrimos(num):
    count = []
    for i in range(2, num):
        if (num % i == 0):
            count.append(i)
    for x in count:
        if num % x == 0 and 3 % x == 0:
            return x


print(divisoresPrimos(24))

