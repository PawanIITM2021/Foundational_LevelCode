i=int(input())
def prime(i):

    if i>=2:
        for j in range(2,i):
            if i%j != 0:
                return 'Prime'
            else:
                return 

print(prime(i))