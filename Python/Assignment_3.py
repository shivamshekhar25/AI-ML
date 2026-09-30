
#Q1

word = input("Enter a word: ")

reverse = ""

for i in range(len(word)-1, -1, -1):
    reverse += word[i]

if word == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#Q2

numbers = [10, 20, 30, 40, 50]
sum = 0
for num in numbers:
    sum += num
average = sum / len(numbers)
print("Average =", average)


#Q3

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

list3 = list1 + list2

list3.sort()

print("Merged and sorted list:", list3)



#Q4

tup = (1, 2, 3, 4, 5, 6, 7, 8)

even = ()
odd = ()

for num in tup:
    if num % 2 == 0:
        even += (num,)
    else:
        odd += (num,)

print("Even numbers:", even)
print("Odd numbers:", odd)


#Q5

students = {}

while True:
    print("\nA - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        students[name] = marks
        print("Student added successfully.")

    elif choice == "B":
        name = input("Enter student name: ")

        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    elif choice == "C":
        name = input("Enter student name: ")

        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found.")

    elif choice == "D":
        if len(students) == 0:
            print("No students found.")
        else:
            for name, marks in students.items():
                print(name, ":", marks)

    elif choice == "E":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")


#Q6

words = ["apple", "banana", "kiwi", "cherry", "mango"]

result = {}

for word in words:
    result[word] = len(word)

print(result)



#Q7

string = input("Enter a string: ")

count = 0

for char in string:
    if char == " ":
        count += 1

print("Number of spaces:", count)




#Q8


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

if len(common) == 0:
    print("No common elements")
else:
    print("Common elements exist")



#Q9

list1 = [1, 2, 3, 2, 4, 1, 5]

seen = set()
duplicate = set()

for num in list1:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)

print("Duplicate elements:", duplicate)


#Q10

word=input("enter a word:")
count=0
for i in word:
    print(i)
    count+=1
print(count)

              #or


string = input("Enter a string: ")

unique = set(string)

print("Unique characters:", unique)
print("Count of unique characters:", len(unique))