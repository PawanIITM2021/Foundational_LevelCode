def value_to_keys(D,value):
    keys = []
    for key in D:
        if D[key] == value:
            keys.append(key)
    return keys

def one_to_one(D):
    for value in D.values():
        if len(value_to_keys(D,value)) !=1:
            return False
    return True