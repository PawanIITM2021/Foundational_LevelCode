def is_perfect(num):
    #Factor sum
    fsum = 0
    for f in range(1,num):
        if num % f == 0:
            fsum += f
    #fsum == num is a Boolean expression
    #It will evaluate to True if num is a perfect number
    #And False Otherwise
    return fsum == num

print(is_perfect(int(input())))
