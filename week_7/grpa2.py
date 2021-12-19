D1={1:2,2:3,3:4}

D2={1:10,4:15,5:10}

priority='first'


'''
def merge(D1, D2, priority):
    d={}
    if priority=='first':
        for key in D1:
            d[key]=D1[key]
        for key in D2:
            if key not in D1:
                d[key]=D2[key]
    elif priority=='second':
        for key in D2:
            d[key]=D2[key]
        for key in D1:
            if key not in D2:
                d[key]=D1[key]
    return d

print(merge(D1, D2, priority))
'''


# The basic ideas is to write the code for priority equal to "first"
# when priority is "second", we can just reverse the order of the dicts
def merge(D1,D2,priority):
    if priority == 'second':
        return merge(D2, D1, 'first')
    D = dict()
    # first copy all key-value pairs in D1 to D
    for key in D1:
        value = D1[key]
        D[key] = value
    # Copy all those key-value pairs in D1 to D where the key is not already present in D
    for key in D2:
        value = D2[key]
        if key not in D:
            D[key] = value
    return D
    
print(merge(D1, D2, priority))









