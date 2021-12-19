def multiply(a,b):
    if b==1:
        return a
    else:
        sum = a + multiply(a,b-1)
        return sum

print(multiply(5,4))
    