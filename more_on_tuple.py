t =1,2,3 #packing
print(t, type(t))

x,y,z = t #unpacking
print(x,y,z)

x=5
y=10
x,y = y,x
print(x,y)

l=[10]
print(l,type(l))

t=(10)
print(t,type(t))

t=(10,)
print(t,type(t))

t = ([1,2], ['a', 'b'])
t[0][0] = 25
print(t)

t1 = (1,2,3)
t2 = ([1,2,3],)

t2[0][1]=9
print(t2)