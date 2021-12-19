mysterious=''
def type_of_sequence(L):
    k=0
    for word in L:
        if mysterious(word):
            k+=1
    if k < 2:
        return 'midly mysterious'
    elif 2<=k<5 :
        return 'moderately mysterious'
    elif k>=5 :
        return 'most mysterious'
        