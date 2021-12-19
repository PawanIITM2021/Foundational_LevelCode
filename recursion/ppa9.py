def uniq(L):
    if len(L)==1:
        return [L[0]]  
    else:
        if L[0] not in L[1:]:
            new_L = [L[0]] + uniq(L[1:])
            return new_L
        else:
            new_L = uniq(L[1:])
            return new_L
        
    
   
    

print(uniq([10,9,6,9,10,6,10]))