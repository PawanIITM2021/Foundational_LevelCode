dim=int(input())
mat=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    mat.append(row)
for i in range(dim):
    L=len(mat[i])
    for j in range(L):
        if j<L-1:
            print(mat[i][j],end=' ')
        else:
            print(mat[i][j])

print('------ matrix rotated by 90 degree-------')

def rotate(mat):
    rotated=[]
    for i in range(len(mat[0])):
        turned=[]
        for j in mat[::-1]:
            turned.append(j[i])
        rotated.append(turned)
    return rotated

print(rotate(mat))