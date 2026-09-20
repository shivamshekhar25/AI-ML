username=input("enter Your Username:")
password=input("enter your password:")
if username=="admin" and password=="pass":
    print("login successful")
else:
    if username!="admin":
        print("username is wrong")
    else :
        print("password is wrong")