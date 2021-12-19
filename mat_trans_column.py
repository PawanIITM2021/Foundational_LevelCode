'''
1 2 3               3 2 1
4 5 6      to       6 5 4
7 8 9               9 8 7

'''

dim=int(input())
A=[]

for i in range(dim):
    row=[]
    for j in input().split(','):
        row.append(int(j))
    A.append(row)
print(A)

for i in range(dim):
    for j in range(1,dim+1):
        if j!=dim:
           print(A[i][-j],end=' ')
        else:
            print(A[i][-j])


