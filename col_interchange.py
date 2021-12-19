dim=int(input())
mat=[]
for i in range(dim):
        row=[]
        for j in input().split(','):
            row.append(int(j))
        mat.append(row)
print(mat)


# printing colume interchange
for i in range(len(mat)):
    for j in range(len(mat[i])-1,-1,-1):
        if j>0:
            print(mat[i][j],end=' ')
        else:
            print(mat[i][j])



# making matrix of col interchange    
col_intrchng=[]
for i in range(len(mat)):
    col_intrchng.append([])
for i in range(len(mat)):
    for j in range(len(mat)-1,-1,-1):
        col_intrchng[i].append(mat[i][j])
print(col_intrchng)


        