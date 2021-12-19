def non_decreasing(L):
    if len(L)==1 or len(L)==0:
        return True
    else:
        if L[0]<=L[1]:
            return non_decreasing(L[1:])
        else:
            return False

print(non_decreasing([10,1,100,1000,10000]))