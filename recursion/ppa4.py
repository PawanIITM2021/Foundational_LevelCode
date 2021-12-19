def logarithm(x):
    if x==1:
        return 0
    else:
        sum = 1 + logarithm(x//2)
        return sum

print(logarithm(32))