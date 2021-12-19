# Accept a positive integer n as input, where n is greater than 1. Print PRIME if n is a prime number and NOTPRIME otherwise.

num = int(input())

count=0
if num>=2:
    for i in range(num):
        for j in range(2,i):
            if num%j ==0:
                count=count + 1

if count==0:
    print('PRIME')
else:
    print('NOTPRIME')
