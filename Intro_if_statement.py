#if Condition
#Let us consider the movie "Avengers". This is a 13+ movie

print("Please enter your date of birth's year")
birth_year=int(input())

current_year=2021
age=current_year-birth_year

if(age<13):
    print("You are under age, you cannot watch this movie")
else:
    print("You are old enough to watch Avengers, enjoy!")

print("Have a nice time")


