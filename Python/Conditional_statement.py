age=int(input("Enter Your age :"))
if age>=18:
    print("You are eligible for vote")
    print("You are eligible for vicle driving")
else:
    print("Not Eligble for anyone")



color=str(input("enter a color:"))
if color=="red":
    print("Stop")
elif color=="yellow":
    print("look")
elif color=="green":
    print("Go")
else:
    print("Not Exit Color !")


Age=int(input("enter your age:"))
if Age<13:
    print("Child")
elif Age>=13 and Age<=18:
    print("Teen Age")
else:
    print("Adult")


username=input("Enter Your Username:")
password=input("Enter your password:")
if username=="Admin" and password=="pass":
    print("Login Successful")

elif username!="Admin" and password!="pass":
    print("username and password both is Wrong Pls try Again")

elif username!="Admin":
    print("Username is Wrong")

else:
    print("Password is Wrong")






n=int(input("Enter a Number:"))
if n%5==0:
    print("Number is multiple of 5")
else:
     print("Number is not MULTIPLE OF 5")



N=int(input("enter a number:"))
if N%2==0:
    print("Number is Even")
else:
    print("Number is odd")