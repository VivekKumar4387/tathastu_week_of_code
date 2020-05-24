x=-1
y=1
z=0
numb=int(input("enter a limit"))
for i in range(0,numb):
    z=x+y
    print(z,end=",")
    x=y
    y=z
