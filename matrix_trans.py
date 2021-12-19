dim=int(input())
matrix=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    matrix.append(row)
print(matrix)

for i in range(len(matrix[0])):
    for j in range(dim):
        if j<dim-1:
            print(matrix[j][i],end=' ')
        else:
            print(matrix[j][i])

    


