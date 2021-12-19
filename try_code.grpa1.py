a=int(input())
b=int(input())
c=int(input())

x=a*a
y=b*b
z=c*c

if(((x+y)==z) or ((y+z)==x) or ((z+x)==y)):
    print("YES")
else:
    print("NO")