L=[70,49,39,58,86,48,98,58,98,38,99,88,76,87,10,13]
L=[30,50,40,10,20]
L=[100,20,10,100,30,70,40,60,10,50,50,50,40,30,70,80,90,10,10,10,10,30]

for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]>L[j]:
            temp=L[i]
            L[i]=L[j]
            L[j]=temp

print(len(L))
print(L)

num=len(L)
if num%2==0:
    n=int((num/2)-1)
    print((L[n]+L[n+1])/2)
else:
    n=(num//2)
    print((L[n])/1)


    





''' Arranging in decending
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]<L[j]:
            temp=L[i]
            L[i]=L[j]
            L[j]=temp

print(L)'''