'''Check Palindrome Or Not'''

# from typing import AbstractSet


# num=int(input('Enter a number:\n'))

# absNum=abs(num)
# rev=absNum%10
# absNum=absNum//10

# while absNum>0:
#     r=absNum%10
#     absNum=absNum//10
#     rev=rev*10+r
# if num<0:
#     rev=rev-2*rev
# if num==rev:
#     print('Palindrome')
# else:
#     print('Not a Palindrome')

num=int(input('Enter a number: '))
absStrnum=str(abs(num))
rev=''
for c in absStrnum:
    rev=c+rev
if num<0 :
    rev = '-' + rev
if (num == int(rev)):
    print("Palindrome")
else:
    print("Not a palindrome")
