sum=lambda a,b: a+b
print(sum(10,20))


print((lambda a,b: a+b)(40,50))





#program  factorial of n number
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))
