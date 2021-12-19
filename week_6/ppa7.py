n=int(input())
scores_dataset=list()
while n>0:
    D = dict()
    D['Name']=input()
    D['City']=input()
    D['SeqNo']=int(input())
    D['Mathaematics']=int(input())
    D['Physics']=int(input())
    D['Chemistry']=int(input())
    scores_dataset.append(D)
    n -= 1
