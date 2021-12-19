L = input().split(',')

max=len(L[0])
for x in L:
    if len(x)>=max:
        max=len(x)
        word=x

print(word)
