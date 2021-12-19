words=['a', 'random', 'collection', 'a', 'another', 'a', 'random']

def freq_to_words(words):
    d={}
    s=set(words)
    for x in s:
        count=words.count(x)
        d[count]=[x]

   
    for text in words:
        count=words.count(text)
        for elem in d[count]:
            if elem!=text:
                d[count].append(text)    
        

    return d
print(freq_to_words(words))
print(set(words))
        

    
        
   
        
