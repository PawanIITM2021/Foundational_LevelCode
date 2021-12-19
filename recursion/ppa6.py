def spiral_iterative(left,right,n):
    for i in range(n-1):
        m = (left + right)/2
        if i%2==0:
            left=m
        else:
            right=m
    return m
def spiral_recursive(left,right,n):
    m=(left+right)/2
    if n==2:
        return m
    else:
        if n%2==0:
            return spiral_recursive(m,right,n-1)
        else:
            return spiral_iterative(left,m,n-1)

print(spiral_recursive(0,1,4))
print(spiral_iterative(0,1,100))