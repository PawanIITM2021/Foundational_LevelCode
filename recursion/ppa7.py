def count(L,word):
    if len(L)==0:
       return 0
    else:
        if L[0] == word:
            return 1 + count(L[1:],word)
        else:
            return count(L[1:],word)




print(count(['good','string','good','again','good','kat','good'],'good'))

