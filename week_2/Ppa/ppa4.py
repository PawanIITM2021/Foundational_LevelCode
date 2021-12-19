x=float(input())
y=float(input())

if x>0:
    if y>0:
        print('first')
    if y<0:
        print('fourth')
elif x<0:
    if y>0:
        print('second')
    if y<0:
        print('third')
else:
    print('origin')
