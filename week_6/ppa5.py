def dict_to_list(D):
    L = []
    for key in D:
        T = (key, D[key])
        L.append(T)
    return L

def list_to_dict(L):
    D = dict()
    for i in range(len(L)):
        D[L[i][0]] = L[i][1]
    return D

# Other method --> Unpacking of tuple
def list_to_dict(L):
    D = dict()
    # L is a list of tuples
    # each element of L is of the form (key,value)

    for (key,value) in L:
        D[key] = value
    return D

