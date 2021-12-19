word_1=input()
word_2=input()
alpha='abcdefghijklmnopqrstuvwxyz'

def distance(word_1, word_2):
    dist=0
    if len(word_1)==len(word_2):
        for i in range(len(word_2)):
            dist += abs(alpha.index(word_1[i]) - alpha.index(word_2[i]))
        return dist
    else:
        return -1
        



print(distance(word_1,word_2))
    
    
