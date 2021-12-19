dict={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,}
e=input().split(' ')
sum=0

i=0
if e[0] in dict:
    sum=sum+dict[e[0]]
    i=1
else:
    if(e[0]=='plus'):
        sum = sum + dict[e[1]]
        i=2
    else:
        sum=sum-dict[e[1]]
        i=2

while(i<len(e)):
    if(e[i]=='plus'):
        sum = sum + dict[e[i+1]] 
    else:
        sum=sum-dict[e[i+1]]
    i=i+2
print(sum)
