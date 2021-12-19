dim=int(input())

matrix_1=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    matrix_1.append(row)

matrix_2=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    matrix_2.append(row)

matrix=[]
for i in range(dim):
    row=[]
    for j in range(dim):
        j=0
        row.append(j)
    matrix.append(row)

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

for i in range(dim):
    for j in range(dim):
        if j<dim-1:
            print(matrix[i][j],end=',')
        else:
            print(matrix[i][j])

print('-----------matrix_1-----------')
print(matrix_1)
print('-----------matrix_2-----------')
print(matrix_2)
print('-----------matrix-----------')
print(matrix)