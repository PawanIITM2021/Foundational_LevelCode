M=[[1,2,3],[4,5,6],[7,8,9]]
i=2
j=0

'''
def minor_matrix(M, i, j):
    for row in range(len(M)):
        if row==i:
            M.remove(M[row])
    for row in range(len(M)):
        for col in range(len(M[row])):
            if col==j:
                M[row].remove(M[row][col])

    return M
print(minor_matrix(M,i,j))
'''

def minor_matrix(M,i,j):
    # dimension of M
    n = len(M)
    # the matrix M_ij
    M_ij = []
    for row in range(n):
        # skip row i
        if row == i:
            continue
        L =[]
        for col in range(n):
            # skip column j
            if col == j:
                continue
            # add all other elements as they are
            L.append(M[row][col])