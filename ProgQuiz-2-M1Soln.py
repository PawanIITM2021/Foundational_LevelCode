def exact_count(para, n):

    c=para.split(' ')
    #good word many works good real choice
    for i in range(len(c)):
        count=0
        for j in range(len(c)):
            if c[i]==c[j]:
                count += 1

        if count==n:
            return True
    return False 