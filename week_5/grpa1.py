#get the maximum
def get_max(L):
    maxi=L[0]
    for x in L:
        if x>maxi:
            maxi = x
    return maxi

#get the minimum
def get_min(L):
    mini=L[0]
    for x in L:
        if x < mini:
            mini=x
    return mini

#get the range
def get_range(L):
    maxi=get_max(L)
    mini=get_min(L)
    return maxi - mini


L=[18.55,7.12,29.56,1.07,24.21,41.01,11.53,10.94,33.63]
print(get_range(L))
