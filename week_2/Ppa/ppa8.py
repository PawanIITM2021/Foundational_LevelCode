INDEX='12345678'
STEP='ABCDEFGH'

start=input()
end=input()

if abs(STEP.index(start[0]))-STEP.index(end[0]) == abs(INDEX.index(start[1])-INDEX.index(end[1])):
    print('YES')
else:
    print('NO')
