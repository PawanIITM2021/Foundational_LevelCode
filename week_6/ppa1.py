# method 1

'''L=input().split(',')

freq =dict()
for word in L:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1'''

# method 2

L=input().split(',')

freq = dict()
for word in L:
    if word not in freq:
        freq[word]=0
    freq[word] += 1

