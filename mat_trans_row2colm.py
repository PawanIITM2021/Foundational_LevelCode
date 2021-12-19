'''
1 2 3               1 4 7
4 5 6       TO      2 5 8
7 8 9               3 6 9

'''

dim=int(input())
A=[]
for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    A.append(row)
print(A)

# Transpose of row to column in matrix A
for i in range(dim):
    for j in range(dim):
        if j != dim-1 :
            print(A[j][i], end=' ')
        else:
            print(A[j][i])
