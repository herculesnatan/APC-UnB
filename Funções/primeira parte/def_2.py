import math as m
def print_twice(bruce):
    print(bruce)
    print(bruce)
# Quando você cria uma variável dentro de uma função, ela é local, ou seja, ela só existe
# dentro da função.

def cat_twice(part_1, part_2):
    cat = part_1 + part_2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tinddle bang.'
cat_twice(line1, line2)


"""""print_twice('Spam')
print_twice(42)
print_twice(m.pi)

print_twice('Spam '*4)
print_twice(m.cos(m.pi))

michael = "Eric, the half a bee."
print_twice(michael)"""""
