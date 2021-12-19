print('Enter the year between 1600 & 9999: ',end=' ')
year=int(input())

def check_leap_year(year):
    if year%100==0 and year%400==0:
        return True
    if year%100!=0 and year%4==0:
        return True
    else:
        return False

print(check_leap_year(year))

