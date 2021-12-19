'''Day wise total rainfall'''

days = int(input('Enter the number of days:'))

for i in range(1, days + 1):
    total=0
    rainfall = int(input('Enter the rainfall:'))
    while(rainfall != -1):
        total = total + rainfall
        rainfall = int(input('Enter the rainfall:'))

    print('Total rainfall for day {0} is {1}'.format(i, total))