st = {1,2,3,4,5}

'''
ordered
duplicate element not allowed
value can be add but element in set not mutable or hashable
'''

A = {1,3,5}
B = {1,2,3,4,5}
print(A.issubset(B))

C1 = A.union(B)
C2 = A | B
print(C1,C2)

C1 = A.intersection(B)
C2 = A & B
print(C1, C2)