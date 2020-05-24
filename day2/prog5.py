a,b=5,3
for i in range(1,4):
    a=a-1
    for j in range(1,a):
        if j--b:
            print(b)
        else:
            print(b,'*',end='')
    b=b-1
for i in range(1,4):
    for l in  range(1,4):
        if l==i:
            print(b)
            break
        else:
            print(b, '*', end='')
