L=[23,45,12,2,36,32,78,56,47,71,29,6,8,35,79,90,86,50]

x=[]
while (len(L)>0):
    mini=L[0]
    for i in range(len(L)):
        if L[i]<mini:
            mini=L[i]
    x.append(mini)
    L.remove(mini)

print(L)
print(x)



     

            