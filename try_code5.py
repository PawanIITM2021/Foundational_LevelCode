x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
x3=float(input())

a=(y1-y2)
b=(x3-x2)
c=(x1-x2)


if (a==0 or b==0 or c==0):
    print("Vertical Line")
elif(c!=0):
    y3=(((a*b)/c)+y2)
    print(y3)
    if(y3>0):
    
        print("Positive Slope")

    elif(y3<0 or y3==0):
    
        print("Negative Slope" or "Horizontal line")



