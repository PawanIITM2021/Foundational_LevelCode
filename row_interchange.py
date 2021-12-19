dim=int(input())
mat=[]
for i in range(dim):
        row=[]
        for j in input().split(','):
            row.append(int(j))
        mat.append(row)
print(mat)

# printing row interchange
for i in range(len(mat)-1,-1,-1):
    for j in range(len(mat[0])):
        if j<len(mat[0])-1:
            print(mat[i][j],end=' ')
        else:
            print(mat[i][j])
    

# make matrix of row_interchange
while len(mat)>0:
    row_reverse=[]
    for i in range(len(mat)-1,-1,-1):
        row_reverse.append(mat[i])
        mat.remove(mat[i])

print(row_reverse)

#print(mat[::-1])


