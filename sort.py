def mini(L):
    '''finds the minimum element in the list L'''
    mini=L[0]
    for x in L:
        if (x<mini):
            mini=x
    return mini

def Sort(L):
    '''recursively sort the list L'''
    if(L==[]) or (len(L)==1):
        return L
    #if the list is empty otherwise  
    
    
    m=mini(L)
    L.remove(m)
    return [m]+Sort(L)

L=[5,6,2,19,59,1,10,1,121]
print(Sort(L))