num = int(input("enter the number"))
p = 1
for i in range(num):
    for j in range(i+1):
        print(p, end = " ")
        p += 1
    print('\n')
