dim=int(input())
mat=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    mat.append(row)

#mat=[[1,2],[3,4],[5,6]]

def transpose(mat):
    len_row=len(mat[0])
    len_col=len(mat)
    mat_trans=[]
    for i in range(len_row):
        t=[]
        for j in range(len_col):
            t.append(mat[j][i])
        mat_trans.append(t)
    return mat_trans

print(transpose(mat))

