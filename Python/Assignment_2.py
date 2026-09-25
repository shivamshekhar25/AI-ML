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



# Q5

def sum_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total


n = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(n))



# Q6


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)



# Q7


while True:
    n = input("Enter a number or Quit: ")

    if n == "Quit":
        break
    n=int(n)

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")



 # Q8

def calculator(a, b, operation):

    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        return a / b

    else:
        return "Invalid operation"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

print("Answer:", calculator(a, b, operation))

# Q9


def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")


# Q10


secret_number = 50

while True:

    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Correct!")
        break

    ##Complete Assignment