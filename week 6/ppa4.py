


def value_to_keys(D, value):
    if value in D.values():
        key_list=[]
        for key in D.keys():
            key_list.append(key)
            for x in key_list:
                if D[x] != value:
                    key_list.remove(x)
        return key_list
    else:
        return []

print(value_to_keys({1: 10, 2: 100, 3: 1000, 4: 10}, 10))