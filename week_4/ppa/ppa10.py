n=int(input())

matrix=[]
matrix_1=[]
matrix_2=[]

for i in range(n):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    matrix_1.append(row)

for i in range(n):
    row=[]
    for j in input().split(","):
        row.append(int(j))
    matrix_2.append(row)

for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    matrix.append(row)
  
print("--------------------Here is the output-------------------------")
for i in range(n):
    for j in range(n):
        matrix[i][j] += matrix_1[i][j] + matrix_2[i][j]
        if j<n-1:
            print(matrix[i][j],end=',')
        else:
            print(matrix[i][j])
    

print('-----------------------------------------------------------')
print(matrix)
print('-----------------------------------------------------------')
print(matrix_1)
print('-----------------------------------------------------------')
print(matrix_2)