n=int(input())

def factorial(n):
    if n>0:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact
    elif n==0:
        fact=1
        return fact
    else:
        return -1

print(factorial(n))