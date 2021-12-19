dim=int(input())
A=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    A.append(row)
for i in range(dim):
    for j in range(dim):
        if j<dim-1:
            print(A[i][j],end=' ')
        else:
            print(A[i][j])
