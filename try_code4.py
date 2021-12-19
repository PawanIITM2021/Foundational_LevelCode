x=float(input())
y=float(input())



if(x>0):
    if(y>0):
        print("first")
    if(y<0):
        print("fourth")
    if(y==0):
        print("x-axis")
elif(x<0):
    if(y>0):
        print("second")   
    if(y<0):
        print("third")
    if(y==0):
        print("x-axis")
    
        
elif(x==0 and y==0):
    print("origin")
    
elif(x==0 and y<0 or y>0):
    print("y-axis")


    

