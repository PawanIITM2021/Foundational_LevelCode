L=input().split(',')
s=set(L)
freq={}
for x in L:
    freq[x]=0

for x in L:
    freq[x]=freq[x]+1

print(freq)
