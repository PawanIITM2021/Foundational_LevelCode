num = int(input("Enter the number : \n" ))
absNum = abs(num)

if num>0 :
    rev = num % 10
    num = num//10

    while(num>0):
        r = num % 10
        num = num//10
        rev= rev*10 + r
    print(rev)

else:
    rev = absNum % 10
    absNum = absNum//10

    while(absNum>0):
        r = absNum % 10
        absNum = absNum//10
        rev= rev*10 + r
    print(rev-2*rev)




