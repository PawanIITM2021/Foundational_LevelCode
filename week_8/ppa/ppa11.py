L1=[2,3,1,7,5]
k=4
L=[1,2,3,5]

def insert(L,x):
    if len(L)>0:
        if x < L[0]:
            return [x]+L
        else:
            return [L[0]] + insert(L[1:],x)
    else:
        return L + [x]


  
print(insert(L,k))
def isort(L):
    if len(L)==1:
        return L
    else:
        return insert(isort(L[1:]),L[0])
print(isort(L))








