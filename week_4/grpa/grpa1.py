words=input().split(' ')
word_taken=input()
count=0
for elem in words:
    if elem==word_taken:
        count += 1
if count>0:
    print('YES')
    print(count)
else:
    print("NO")
        
