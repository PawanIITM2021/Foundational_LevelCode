num=int(input('Enter a number:'))
if (num % 2 ==0): 
    print('Even')
else:
    print('Odd')

num = int(input('Enter a number: '))
if(num % 5==0):
    if(num % 10 == 0):
        print('0')
    else:
        print('5')
else:
    print('Other')

marks=int(input('Enter marks:'))
if(marks >= 0 and marks <= 100):    
    if(marks >= 90):
        print('A')
    if(marks >= 80 and marks < 90):
        print('B')
    if(marks >= 70 and marks <80):
        print('c')
    if(marks >= 60 and marks < 70):
        print('D')
    if (marks < 60):
        print('E')
else:
    print('Invalid input')




marks=int(input('Enter marks:'))
if(marks >= 0 and marks <= 100):    
    if(marks >= 90):
        print('A')
    elif(marks >= 80):
        print('B')
    elif(marks >= 70):
        print('c')
    elif(marks >= 60):
        print('D')
    else:
        print('E')
else:
    print('Invalid input')



print('Travel from city A to city B')
Time = int(input('Enter time: '))
Longer = int(input('Define longer: '))
if(Time >= Longer):
    Price = int(input('Enter Price: '))
    Higher = int(input('Define higher: '))
    if(Price >= Higher):
        print('Train')
    else:
        print('Coach')

else:
    Price = int(input('Enter Price: '))
    Higher = int(input('Define higher: '))
    if( Price >= Higher):
        print('Daytime flight')
    else:
        print('Red eye flight')

print('Arrive City B')




