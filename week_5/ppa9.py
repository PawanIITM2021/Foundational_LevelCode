

def get_column(mat, col):
    dim=len(mat)
    l=[]
    for i in range(dim):
        l.append((mat[i][col]))
    return l
print(get_column(([1,2],[3,4]),0))


def get_row(mat, row): 
    dim=len(mat)
    return mat[row]
print(get_row(([1,2],[3,4]),1))
   