def palindrome(word):
    if len(word)==1 or len(word)==0:
        return True
    else:
        if word[0]==word[-1]:
            return palindrome(word[1:-1])
        else:
            return False

print(palindrome('lemnmel'))
        
