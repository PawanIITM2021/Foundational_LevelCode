para=['good','word','many','good','works','good','real','choice']
n=3

def exact_count(para, n):
    #para=para.split(' ')
    d={}
    for i in para:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    l=d.values()
    for i in l:
        if i==n:
            return True
        else:
            return False
        


           
        
             


print(exact_count(para,n))


