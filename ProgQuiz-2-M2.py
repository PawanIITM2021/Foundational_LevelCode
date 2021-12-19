d={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,}

L=input().split(' ')
sum=0
c=1
for i in L:
    if i=='minus':
        c = -1
        continue
    if i=='plus':
        c=1
        continue

    sum = sum + (c*d[i])

print(sum)
