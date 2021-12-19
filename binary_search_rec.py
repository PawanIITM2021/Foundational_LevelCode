'''Code for binary search, using recursion'''

def rbinarysearch(L,k,begin,end):
    '''This will recursively compute binary search'''
    #if begin and end are the same, then we need to
    #just check L[begin]
    if (begin==end):
        if (L[begin]==k):
            return 1
        else:
            return 0
        
    #if begin and end are consecutive, then check them
    #individually.
    if (end-begin==1):
        if (L[begin]==k) or (L[end]==k):
            return 1
        else:
            return 0
    #if end-begin>1
    if (end-begin>1):
        #compute the middle element
        mid=(begin+end)//2
        if (L[mid]>k):
            #discard the right and retain the left.
            end=mid+1
        if (L[mid]<k):
            #discard the left and retain the right.
            begin=mid+1
        if (L[mid]==k):
            return 1
    return rbinarysearch(L,k,begin,end)

L=list(range(1000*1000*100))
print(rbinarysearch(L,10000,0,len(L)-1))