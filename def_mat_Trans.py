mat=[[1,2,3],[4,5,6],[7,8,9]]

def get_column(mat, col):
    col_list = []
    m=len(mat)
    for row in range(m):
        col_list.append(mat[row][col])
    return col_list

def transpose(mat):
    m,n = len(mat), len(mat[0])
    mat_trans = []
    for i in range(n):
        mat_trans.append(get_column(mat,i))
    return mat_trans
print(transpose(mat))