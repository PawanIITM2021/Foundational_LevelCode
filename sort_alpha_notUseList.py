word=input().lower()
L=len(word)
out_string=''

for char in 'abcdefghijklmnopqrstuvwxyz':
    for i in range(L):
        if char==word[i]:
            out_string += char
print(out_string)