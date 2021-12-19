
dim=int(input())
A=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    A.append(row)

B=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    B.append(row)

C=[]
for i in range(dim):
    row=[]
    for j in range(dim):
         row.append(0)
    C.append(row)

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] += A[i][k] * B[k][j]

for i in range(dim):
    for j in range(dim):
        if j != dim-1:
            print(C[i][j],end=' ')
        else:
            print(C[i][j])
        