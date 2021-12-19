first_S=int(input())**2
second_S=int(input())**2
third_S=int(input())**2

if first_S==second_S + third_S or second_S==third_S + first_S or third_S==first_S + second_S:
    print('YES')
else:
    print('NO')




