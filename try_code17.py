password=str(input())
l=len(password)



if password.find('\\')!=-1 or password.find('/')!=-1 or password.find('=')!=-1 or password.find("'")!=-1 or password.find('"')!=-1:
    print("False")

elif password.isspace():
    print("False")

elif 8<=l<=32 :
    if password[0].isalpha():
        print("True")
    

            
    