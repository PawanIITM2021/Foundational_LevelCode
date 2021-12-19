L=input().split(',')

last=L[0]
lenth=len(L)
x=lenth-1
while lenth>x>0 :
    print(L[x],end=',')
    x -= 1
print(last)