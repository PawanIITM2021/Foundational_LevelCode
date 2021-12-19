#This is popularly called the caesar cipher in cryptography


alpha='abcdefghijklmnopqrstuvwxyz'

i=5
print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])
print(alpha[i+4])
print(alpha[i+5])

print(alpha[20])

i=25
print(alpha[i%13])
print(alpha[i%26])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26])

alpha='abcdefghijklmnopqrstuvwxyz'
s='pawan'
# I expect to output qbxbo

t=''

i=0
k=1
t=t+(alpha[(((alpha.index(s[i]))+k)%26)])
print(t)
t=t+(alpha[(((alpha.index(s[i+1]))+k)%26)])
print(t)
t=t+(alpha[(((alpha.index(s[i+1+1]))+k)%26)])
print(t)
t=t+(alpha[(((alpha.index(s[i+1+1+1]))+k)%26)])
print(t)
t=t+(alpha[(((alpha.index(s[i+4]))+k)%26)])
print(t)
