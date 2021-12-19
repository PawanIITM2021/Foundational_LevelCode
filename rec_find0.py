'''This is a piece of code to check if a given list has
 0 in it or not. if it has 'zero' in it, we return 
 true(1) otherwise we return false(0)'''



def check0(L):
    #if the list is empty, return False
    if (len(L)==0):
        return 0
    if (L[0]==0):
        #if the first element is zero then return 1
        return 1
    else:
        return check0(L[1:len(L)])
    
print(check0([1,2,4,0,5,10,9,7,3]))
        