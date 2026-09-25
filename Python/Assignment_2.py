# Q1

salary=int(input("Enter Your Salary:"))
if salary<30000:
    print("Tax=5%")
elif salary>=30000 and salary<=70000:
    print("Tax=15%")
else:
    print("Tax=25%")

# Q2

def even_number(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)

a=int(input("Enter Starting Number:"))
b=int(input("Enter Ending Number"))

even_number(a,b)

# Q3

def number(n):
    for digit in str(n):
        print(digit)

n=int(input("enter a number :"))

number(n)


# Q4

def count_digits(n):
    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count


n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))
