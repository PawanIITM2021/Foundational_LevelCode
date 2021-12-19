def triangular(n):
    if n==0:
        return 0
    else:
        sum = n + triangular(n-1)
        return sum
print(triangular(10))