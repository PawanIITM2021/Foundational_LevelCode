# method 1 is_key

def is_key(D, key):
    if key in D:
        return True
    else:
        return False

# method 2 is_key

'''def is_key(D, key):
    return (key in D)'''

# method 1 value

def value(D,key):
    if key not in D:
        return D[key]
        

# method 2 value


    