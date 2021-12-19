def is_key(D,key):
    if key in D.keys():
        return True
    else:
        return False

def value(D,key):
    if key in D.keys():
        return D[key]
    else:
        return 