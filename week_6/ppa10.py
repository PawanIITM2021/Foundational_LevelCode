def group_by_city(scores_dataset):
    cities = dict()
    for student in scores_dataset:
        city=student['City']
        name=student['Name']
        name = student['a']
        if city not in cities:
            cities[city]=[]                
        cities[city].append()

    return cities

def busy_cities(scores_dataset):
    cities = group_by_city(scores_dataset)

    busyval = 0
    L=[] #list of busy cities
    for key, value in cities.items():
        if len(value) > busyval:
            busyval = len(value)
            L = [key]
        elif len(value) == busyval:
            L.append(key)
    
    return L



