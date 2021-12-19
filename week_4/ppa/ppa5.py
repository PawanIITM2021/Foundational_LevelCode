L=input().split(' ')


for x in L[:-1]:
    x=float(x)
    x=int(x//1)
    print(x,end=',')
print((int(float(L[-1]))//1))



