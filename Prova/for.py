num_1, num_2 = input().split()
num_1 = int(num_1)
num_2 = int(num_2)

for i in range(2):
    for num in range(num_1,num_2+1, i+1):
        print(num, end=' ')
    print()
