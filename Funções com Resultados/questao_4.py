def max3(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print(max3(27,5,2022))


"""""
print(max3(27,5,2022))
print(max3(1,4,2001))
print(max3(100,200,300))

"""""