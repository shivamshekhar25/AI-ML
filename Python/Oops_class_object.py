class Student:
    Name="Shivam"
    Age=18
    subject="Python"

st1=Student()
st2=Student()
print(st1)


class Student:
    Name="Shivam"
    Age=18
    subject="Python"

st1=Student()
st2=Student()
print(st1.Age)




class Student:
    def __init__(self):
        print("Constructor was Called.")

st1=Student()
st2=Student()
st3=Student()
st4=Student()





class Student:
    def __init__(self,Name):
        self.Name=Name

st1=Student("Rahul")
st2=Student("Shivam")
st3=Student("samridh")
st4=Student("Richa")

print(st1.Name)
print(st2.Name)
print(st3.Name)
print(st4.Name)




class Student:
    def __init__(self,Name,CGPA):
        self.Name=Name
        self.CGPA=CGPA

st1=Student("Rahul",9.0)
st2=Student("Shivam",9.8)
st3=Student("samridh",6.5)
st4=Student("Richa" ,7.8)

print(st1.Name,st1.CGPA)
print(st2.Name)
print(st3.Name)
print(st4.Name)




class Student:
    def __init__(self,Name,CGPA):
        self.Name=Name
        self.CGPA=CGPA
    def get_cgpa(self):
        return self.CGPA
        

st1=Student("Rahul",9.0)
st2=Student("Shivam",9.8)
st3=Student("samridh",6.5)
st4=Student("Richa" ,7.8)


print("Rahul Cgpa:",st1.get_cgpa())






