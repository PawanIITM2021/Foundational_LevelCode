a=str(input())

if((len(a)%2)!=0 and len(a)>=7):
    print(a[((len(a)//2)-1):((len(a)//2)+2)])

if(len(a)%2==0):
    print(a[((len(a)//2)-2):((len(a)//2)+1)])