string=input().lower()
VOW_L='aeiou'

for i in VOW_L:
    if i in string:
        print(i,end='')