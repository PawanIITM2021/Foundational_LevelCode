num=input().split(',')
a=int(num[0])
b=int(num[1])
c=int(num[2])

def maxval(a,b,c):
    if a>b and a>c:
        max=a
    elif b>a and b>c:
        max=b
    else:
        max=c
    return max

print(maxval(a,b,c))

  

