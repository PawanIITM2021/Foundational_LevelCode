# A raised to the power m
# A -> m times

def zero_matrix(n):
    '''zero matrix of size n * n'''
    M = []
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(0)
        M.append(row)
    return M

def mat_mul(A,B):
    '''multiply A and B'''
    n = len(A)
    prod = zero_matrix(n)
    # multiply A and B
    for i in range(n):
        for j in range(n):
            for k in range(n):
                prod[i][j] += A[i][k] * B[k][j]
    return prod

def power(A,m):
    if m==1:
        return A
    A_min_one = power(A,m-1)
    return mat_mul(A_min_one,A) 



# power(A,2)
# A X A
# A_min_one = power(A,1) -> A

# power(A,5)   ->  A X A**4
# power(A,4)   ->  A X A**3
# power(A,3)   ->  A X A**2
# power(A,2)   ->  A X A**1


    