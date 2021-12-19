password=input()


if 8<= len(password) <= 32:
    if type(password[0])==str:
        if  '/'  not in password:
            if '\\' not in password:
                if '=' not in password:
                    if '"' not in password:
                        if "'" not in password:
                            print(True)
                        else:
                            print(False)
                    else:
                        print(False)
                else:
                    print(False)
            else:
                print(False)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)


