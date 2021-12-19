L=input().split(',')

def first_three(L):
    for i in range(len(L)):
        L[i]=int(L[i])
        for j in range(i+1,len(L)):
            L[j]=int(L[j])
            if L[j]<L[i]:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
    fmax=L[-1]
    smax=L[-2]
    tmax=L[-3]

    return fmax,smax,tmax
print(first_three(L))




        

