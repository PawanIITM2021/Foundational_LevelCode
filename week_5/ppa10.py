L=[1,2,3,5]
X=4

def insert(L,X):
    L.append(X)
    n=len(L)
    for i in range(n):
        for j in range(i+1,n):
            if L[j]<L[i]:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
    return L

print(insert(L,X))
                