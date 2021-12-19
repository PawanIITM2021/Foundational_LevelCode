L=[12,15,100,121,1001,1024,2016,2021]

def obvious_search(L,k):
    '''Check if a given element k is present in a list
    L or not. This function was authored by S.R.S. 
    Iyenger'''
    for x in L:
        if x==k:
            return 1
    return 0
    #code verified. working fine.
    
'''A question: Can we write a piece of code that searches
for a given element in the list L faster than the obvious
algorithm
given above :-( :-('''
                   
                
def binary_search(L,k):
    '''This function is an alternative for the obvious
    search. It does exactly what is expected from the
    obvious_search, but in binary search.'''
    
    #We want to shrink my list
    #We will do that using a while loop
    
    begin=0 #first element in L.L[0]
    end=len(L)-1 #the last element in L is in len(L).L[len(L)-1]
    
    #Use a while loop to look at the list and keep halving it.
    while(end-begin>1):
        #We will handle the case when the number of element
        #is less than or  equal to 1
        
        #Compute the mid which is the mid point of begin to end.
        mid=(begin+end)//2
        #if mid is indeed k, then we return True and stop the code.
        if (L[mid]==k):
            return 1
        
        
        #if the middle element is greater than k, then
        #cut the right side and retain the left side.
        if (L[mid]>k):
            end=mid-1
            
            
        #if the middle element is less than k, then
        #cut the left side and retain the right side
        if (L[mid]<k):
            begin=mid+1
            
#This is outside the while loop. if we are here, it means that we
#haven't found the element. Also, if we are here, it
#means that the while condition is voileted. which
#means end-begin is less than or equal to 1.

#if it is equal to 1. it mean begin is equal to end 
#that is exactly two element

    if (L[begin]==k) or (L[end]==k):
        return 1
    else:
        return 0
            
print(binary_search(L,15))