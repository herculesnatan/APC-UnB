def deivis_sequence(d):
    if d == 0:
        return 0
    elif d == 1:
        return 1
    else:
        return deivis_sequence (d-1) + deivis_sequence (d-2)
print(deivis_sequence(10))