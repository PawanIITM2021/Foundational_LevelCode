L=[1,2,3,4]
k=2

def search(L,k):
    if L==[]:
        return False
    else:
        if L[0]==k:
            return True
        else:
            return search(L[1:],k)

print(search(L,k))
        