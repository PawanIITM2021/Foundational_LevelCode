A=[[1,2],[3,4]]
B=[[5,6],[7,8]]

C=[[2,3,4],[6,7,8],[3,2,6]]
D=[[8,7,6],[9,4,2]]

def dim_equal(A,B):
    if len(A)==len(B):
        return True
    else:
        return False

print(dim_equal(A,B))
print(dim_equal(C,D))
