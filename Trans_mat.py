dim=int(input())
mat=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    mat.append(row)
print(mat)








m=len(mat[0])
n=len(mat)
trans_mat=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(mat[j][i])
    trans_mat.append(row)
print(trans_mat)
        