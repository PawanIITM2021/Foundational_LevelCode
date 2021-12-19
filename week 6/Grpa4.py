#scores=[('Harish',80),('Aparna',90),('Harshita',80)]
scores=[('Sachin',85),('Yuvan',65),('Anita',85)]

def two_level_sort(scores):
    for i in range(len(scores)):
        j=i+1
        while j<len(scores):
            if scores[i][1]>scores[j][1]:
                temp=scores[i]
                scores[i]=scores[j]
                scores[j]=temp
                j=i+1
            else:
                j+=1
    
    for i in range(len(scores)):
        for j in range(i+1,len(scores)):
            if scores[i][1]==scores[j][1]:
                if scores[i][0]>scores[j][0]:
                    temp=scores[i]
                    scores[i]=scores[j]
                    scores[j]=temp
                return scores

print(two_level_sort(scores))

  

