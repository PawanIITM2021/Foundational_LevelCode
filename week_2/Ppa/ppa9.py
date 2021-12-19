number_coins=int(input())
first_S=int(input())
second_S=int(input())
third_S=int(input())

if number_coins > 0:
    if first_S>0 and second_S>0 and third_S>0:
        if first_S!=second_S!=third_S:
            if first_S + second_S + third_S == number_coins:
                print('FAIR')
            else:
                print('UNFAIR')
        else:
            print('UNFAIR')
    else:
        print('UNFAIR')
else:
    print('UNFAIR')