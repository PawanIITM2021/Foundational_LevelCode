num = (int(input('Enter a number: ')))
absNum = abs(num)
if(num >= 0):
    rev = num % 10
    num= num//10

    while(num > 0):
        r = num % 10
        num = num//10
        rev = rev*10 + r
    print(rev)

else:
    rev=absNum % 10
    absNum= absNum // 10
    while (absNum>0):
        r= absNum % 10
        absNum = absNum // 10
        rev = rev *10 + r
    print(rev - 2*rev)




# num = int(input('Enter a Number: '))
# absNum = abs(num)
# rev = absNum % 10
# absNum = absNum // 10
# while(absNum > 0):
#     r = absNum % 10
#     absNum = absNum//10
#     rev = rev * 10 + r
# if(num >= 0):
#     print(rev)
# else:
#     print(rev - 2 * rev)
