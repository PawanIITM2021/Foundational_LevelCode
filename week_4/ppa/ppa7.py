n=int(input())
matrix=[]
for x in range(n):
    row=[]
    for y in input().split(','):
        row.append(int(y))
    matrix.append(row)
print(matrix)
        
