L=[1,2,3]
x_0=5

def poly(L, x_0): 
    if len(L)==1:
        return L[0]
    else:
        sum=L[0]+poly(L[1:],x_0)*x_0
        return sum

print(poly(L, x_0))
