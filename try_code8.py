L= int(input())

word= input()
space= ' '
if len(word)<L:
    word= 'short' + space + word
elif L <= len(word) < 2*L:
    word = 'medium' + space + word
else:
    word = 'long' + space + word
print(word)