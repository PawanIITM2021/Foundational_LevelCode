mat=[]
def matrix(dim):
    for i in range(dim):
        row=[]
        for j in input().split(','):
            row.append(int(j))
        mat.append(row)
    return mat

print(matrix(4))

def get_row(mat,i):
    row=[]
    for k in range(len(mat[0])):
        row.append(mat[i][k])
    return row

print(get_row(mat,2))

def get_column(mat,i):
    col=[]
    for k in range(len(mat)):
        col.append(mat[k][i])
    return col

print(get_column(mat,2))
