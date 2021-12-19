def matmulti(m,n):
    mat=[]
    for i in range(len(m)):
        a=[]
        for j in range(len(m)):
            b=0
            for k in range(len(m)):
                b+=m[i][k]*n[k][j]
            a.append(b)
        mat.append(a)
    return mat

def power(A,m):
    if m==1:
        return A
    else:
        return matmulti(A,power(A,m-1))
        
