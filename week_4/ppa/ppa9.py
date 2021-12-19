n=int(input())
matrix=[]

for i in range(n):
    row=[]
    for j in input().split(' '):
        row.append(int(j))
    matrix.append(row)

mul=int(input())
for i in range(n):
    for j in range(n):
        matrix[i][j] *= mul
        if j<n-1:
            print(matrix[i][j],end=' ')
        else:
            print(matrix[i][j])
        
