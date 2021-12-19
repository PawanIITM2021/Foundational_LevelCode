def minor_matrix(M,i,j):
    M_ij = []
    n = len(M)
    for row in range(n):
        if row == i:
            continue
        L=[]
        for col in range(n):
            if col == j:
                continue
            L.append(M[row][col])
        M_ij.append(L)
    return M_ij

def det(M):
    if len(M)==2:
        d=M[0][0] * M[1][1] - M[0][1] * M[1][0]
        return d

    val = 0
    for j in range(len(M)):
        val = val + ((-1)**j)*M[0][j]*det(minor_matrix(M,0,j))
    return val


