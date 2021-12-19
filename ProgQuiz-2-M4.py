L=[1,2,3]


def subsets(L):
    if len(L)==1:
        return [[],L]
    else:
        l=[]
        for sub in subsets(L[0:-1]):
            l.append(sub)
            l.append([L[-1]])
            l.append(sub+[L[-1]])
    t=[]
    for i in l:
        if i not in t:
            t.append(i)
    return t

print(subsets(L))

