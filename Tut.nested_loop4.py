'''Find the length of longest word'''

word = input('Enter a word: ')
maxLen = 0
while(word != '-1'):
    count=0
    for letter in word:
        count = count + 1
    if(count > maxLen):
        maxLen = count
    word = input('Enter a word: ')
print('The length of longest word is %s' %maxLen)