names=input().split(',')
D_O_B=input().split(',')
n=len(names)

for i in range(n):
    D_O_B[i] = int(D_O_B[i])

common = []
for i in range(n):
    for j in range(n):
        if ((i != j) and (D_O_B[i] == D_O_B[j]) and names[i] < names[j]):
            pair = [names[i], names[j]]
            common.append(pair)
print(common)
