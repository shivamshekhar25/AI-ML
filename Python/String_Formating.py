string="shiavm"
print("my name is : {}" .format(string))



# normal formatting
a=5
b=19
sum=a+b
print("sum is :{}" .format(sum))
print("num{} and num{} of sum {}" .format(a,b,sum))

#index bassed formatting
a=5
b=19
sum=a+b
print("sum is :{}" .format(sum))
print("num{1} and num{0} of sum {2}" .format(b,a,sum))

#Value Bassed formating
print("first num{a},and second num {b}".format(a=5,b=7))

