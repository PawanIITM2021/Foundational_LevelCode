n=int(input())
l=input().split(',')
p=[]
max=0
for i in range(len(l)):
    for j in range(len(l)):
        s=0
        if i+j==(n-2):
            s=int(l[i]) + int(l[j])
            p.append(s)
        p.append(int(l[-1]))
for i in range(len(p)):
    if p[i]>max:
        max=p[i]
print(max)
            
    
    



    