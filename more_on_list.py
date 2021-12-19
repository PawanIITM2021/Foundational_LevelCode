l1 = [1,2,3]
l2 = [10,20,30]

l12 = l1 + l2
l21 = l2 + l1
print(l12,l21)

l3 = [0] * 10
print(l3)

l4=[1,2,3]
l5=[1,2,3]
l6=[1,3,2]

print(l4==l5)
print(l5==l6)


print([1,2] < [2,1])
print([2,3] < [3])
print([1]<[1,2,3])
print([]<[1])

l = [1,2,4]
print(l)
l[2]=3
print(l)

l1 = [1,2,3]
l2 = l1
l1[0] = 100
print(l1,l2)

l1 = [1,2,3]
l2 = list(l1)
l3 = l1[:]
l4 = l1.copy()

l2[0] = 100
l3[1] = 200
l4[2] = 300

print(l1, l2, l3, l4)

def add(x):
    x.append(1)
    return(x)

x = [5]
print(add(x))
print(x)

l = [1,2,3]
print(l)

l.append(4)
print(l)

l.insert(2,9)
print(l)

l.remove(2)
print(l)

l.pop(0)
print(l)

l=[2,6,1,50,3,7,5]
l.sort()
l.reverse()
print(l)

