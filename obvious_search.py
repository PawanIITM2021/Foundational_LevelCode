'''Check if a given element k is present in a list L or not'''

def obvious_search(L,k):
    for x in L:
        if x==k:
            return 1
    return 0 

L=list(range(100))
print(L)
print(obvious_search(L,76))
#code verified. working fine

def sum(n):
    ans=0
    for i in range(n):
        ans += i
    return ans


import time

a=time.time();print(sum(1000000));b=time.time();print(b-a)

