# Accept a integer as input and print all the primes less than num with space between them

num=int(input())

primes=[]

for i in range(2,num+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        primes.append(i)
print(primes)
