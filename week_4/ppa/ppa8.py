n=int(input())

matrix=[]
for i in range(n):
    row=[]
    for j in range(n):
        j=0
        row.append(j)
    matrix.append(row)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i==j:
            matrix[i][j]+=1
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if j<n-1:
            print(matrix[i][j],end=',')
        else:
            print(matrix[i][j])

    