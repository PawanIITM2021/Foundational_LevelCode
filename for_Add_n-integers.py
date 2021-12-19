#Adds the first n integers

n=int(input('Enter a number: '))
ans=0
for i in range(n+1):
    ans=ans+i
print("The answer is: ",ans)
