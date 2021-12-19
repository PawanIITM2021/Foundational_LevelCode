dim=int(input())
mat=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    mat.append(row)



def get_column(mat,col):
    column_list=[]
    for i in range(len(mat)):
        column_list.append(mat[i][col])
    return column_list
        
print(get_column(mat,1))

def get_transpose(mat):
    transpose=[]
    for i in range(len(mat[0])):
        transpose.append(get_column(mat,i))
    return transpose

print(get_transpose(mat))