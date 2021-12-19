import random

l=[]
#create an empty list.
for i in range(30):
    l.append(random.randint(1,365))
    #append random numbers between 1 to 365
    #append 30 of them
l.sort()
print(l)
i=0
flag=0 #Denotes that there is no repetition
while(i<len(l)-1):
    if (l[i]==l[i+1]):
        print('Repeats',l[i],l[i+1])
        flag=1
        break
    i=i+1
    
if (flag==0):
    print('There is no repetition')
        





