fp=input()
fpd=input()
sp=input()
spd=input()



if fpd[6:]<spd[6:]:
    print(sp)
elif fpd[6:]>spd[6:]:
    print(fp)
elif fpd[6:]==spd[6:]:
    if fpd[3:5]<spd[3:5]:
        print(sp)
    if fpd[3:5]>spd[3:5]:
        print(fp)
    elif fpd[3:5]==spd[3:5]:
        if fpd[0:2]<spd[0:2]:
            print(sp)
        if fpd[0:2]>spd[0:2]:
            print(fp)
   


