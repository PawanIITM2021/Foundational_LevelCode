'''Reverse the digits of input number'''

# num=int(input())
# absNum=abs(num)
# rev=absNum%10
# absNum=absNum//10
# while absNum>0:
#     r=absNum%10
#     absNum=absNum//10
#     rev=rev*10+r
# if num>0:
#     print(rev)
# else:
#     print(rev-2*rev)

num=int(input('Enter a number: '))
absStrNum = str(abs(num))
rev=''
for c in absStrNum:
    rev=c+rev
if num>=0:
    print(rev)
else:
    print('-' + rev)