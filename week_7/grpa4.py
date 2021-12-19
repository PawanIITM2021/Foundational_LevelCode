'''  INPUT------->
2
Mumbai Express
2
S1,10
S2,20
Chennai Express
3
S1,5
S2,10
S3,15
'''

'''
OUTPUT--------->
{'mumbaiexpress': {'s1': '10', 's2': '20'}, 'chennaiexpress': {'s1': '5', 's2': '10', 's3': '15'}}
'''



def compartment(m):
    compartment_passenger=[]
    D=dict()
    for i in range(m):
        row=[]
        for j in input().split(','):
            row.append(j)
        compartment_passenger.append(row)
    for i in compartment_passenger:
        for j in compartment_passenger:
            D[j[0]]=j[1]
    return D

count=0
Num_Trains=int(input())
d=dict()
while count<Num_Trains:
    Train_name=input()
    m=int(input())
    d[Train_name]=(compartment(m))
    count += 1

print(d)
