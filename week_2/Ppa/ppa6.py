string=input()
if len(string)%2==0:
    string=string+'.'
if len(string)%2!=0:
    dex=len(string)//2
    print(string[dex-1:dex+2])