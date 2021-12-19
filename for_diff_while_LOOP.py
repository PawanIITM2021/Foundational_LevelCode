'''Factorial using for loop'''

num=int(input('Enter a number:\n'))
fact = 1
if num<0 :
    print('not defined')

else:
    for i in range(num,1,-1):
        fact=fact*i

    print(fact)