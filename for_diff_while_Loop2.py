'''Find the number of digits'''
num=abs(int(input('Enter a number: ')))

digits=1
while(num>=10):
    num=num//10
    digits = digits + 1
print(digits)