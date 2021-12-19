num = input()
L = num.split(',')

max=int(L[0])
for x in L:
    x=int(x)
    if x>max:
        max=x

print(max)
    


