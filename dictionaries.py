d={}

d['sudarshan']=9898989898
d['ramya']=7878787878
d['ravi']=9879879876



malgudi=['It','was','monday','morning','swaninathan','was','reluctant','to','open','his','eyes']

s=set(malgudi)

print(s)

d={}
max=0
ans_word=''
for x in s:
    d[x]=0

for x in malgudi:
    d[x]=d[x]+1
    if d[x]>max:
        max=d[x]
        ans_word=x
    
print(d)
print('most frequent value: ',max)
print('most frequent word: ',ans_word)