T=int(input())
if T<0:
    print('INVALID')
if 0<=T<=5:
    print('NIGHT')
if 6<=T<=11:
    print('MORNING')
if 12<=T<=17:
    print('AFTERNOON')
if 18<=T<=23:
    print('EVENING')
if T>=24:
    print('INVALID')