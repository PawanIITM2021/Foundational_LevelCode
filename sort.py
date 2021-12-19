l=[5,2,9,6,1,3,9,0,14,2,23,56,34,12,89,74]

sort_L=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp


print(l)