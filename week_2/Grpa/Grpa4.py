name1=input()
DOB1=input()
day1=int(DOB1[0:2])
month1=int(DOB1[3:5])
year1=int(DOB1[6:])

name2=input()
DOB2=input()
day2=int(DOB2[0:2])
month2=int(DOB2[3:5])
year2=int(DOB2[6:])

if year1 > year2 :
    print(name1)
elif year2 > year1 :
    print(name2)
elif year1 == year2:
    if month1 > month2:
        print(name1)
    elif month1 < month2:
        print(name2)
    elif month1 == month2:
        if day1 > day2:
            print(name1)
        elif day2 > day1:
            print(name2)
        else:
            if name1<name2:
                print(name1)
            if name2<name1:
                print(name2)



