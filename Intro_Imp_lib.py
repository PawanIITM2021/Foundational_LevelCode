import math
import random
print(math.log(10))
print(math.sin(90))
print(math.sqrt(3))
print(math.factorial(6))


print(random.random())

#Let us simulate a coin toss.


a=random.random()

if (a<.5):
    print("Heads")
else:
    print("Tail")

#Stimulate a Dice (six faced)
import random
print(random.randrange(1,7))

dice1=(random.randrange(1,7))
dice2=(random.randrange(1,7))
total=dice1+dice2

print("Your pair of dice is :", total)





