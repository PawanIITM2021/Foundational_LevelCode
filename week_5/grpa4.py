dim=int(input())
mat=[]
for i in range(dim):
    row=[]
    for j in input().split(' '):
        row.append(int(j))
    mat.append(row)

print(mat)


#mat=[[1,2,3],[3,2,1],[1,3,2]]

def row_chk(mat):
    sum=0
    L=[]
    for i in range(len(mat)):
        for j in range(len(mat)):
            sum += mat[i][j]
        L.append(sum)
        sum=0

    return L
print(row_chk(mat))

def col_chk(mat):
    sum=0
    L=[]
    for i in range(len(mat)):
        for j in range(len(mat)):
            sum += mat[j][i]
        L.append(sum)
        sum=0
    return L
print(col_chk(mat))

def d1_chk(mat):
    sum=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i==j:
                sum += mat[i][j]
    return sum
print(d1_chk(mat))

def d2_chk(mat):
    sum=0
    j=len(mat)
    for i in range(len(mat)):
        j -= 1
        sum += mat[i][j]
    return sum
print(d2_chk(mat))


def is_magic(mat):
    if row_chk(mat)==col_chk(mat) and d1_chk(mat)==d2_chk(mat):
        return 'YES'
    else:
        return 'NO'
print(is_magic(mat))





