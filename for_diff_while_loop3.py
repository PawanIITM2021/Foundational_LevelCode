'''Find the number of digits'''

num=abs(int(input('Enter a number: ')))
strNum=str(num)
digits=0
for d in strNum:
    digits = digits + 1
print(digits)