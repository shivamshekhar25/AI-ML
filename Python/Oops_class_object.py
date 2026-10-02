class Student:
    Name="Shivam"
    Age=18
    subject="Python"

st1=Student()
st2=Student()
print(st1)

#-----------------------------------------------------------------------------

class Student:
    Name="Shivam"
    Age=18
    subject="Python"

st1=Student()
st2=Student()
print(st1.Age)


#-----------------------------------------------------------------------

class Student:
    def __init__(self):
        print("Constructor was Called.")

st1=Student()
st2=Student()
st3=Student()
st4=Student()


#------------------------------------------------------------------------------


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


#--------------------------------------------------------------------

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


#--------------------------------------------------------------------------

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

#--------------------------------------- Attributes- Class and instance

class Student:
    clg_name="SU" #class attribute
    PI=3.5

    def __init__(self,name,gpa):
        self.name=name #Instance attribute
        self.gpa=gpa
        self.PI=4.5

st1=Student("Shivam",9.8)

print(st1.name)
print(Student.name)   #=>Error
print(st1.clg_name)
print(st1.PI)  #instace Attribute Higher Priority
print(Student.PI)



#-------------------------------------------------Instance Method

class Laptop:
    Storage_type="SSD"

    def __init__(self,Ram,Storage):
        self.Ram=Ram
        self.Storage=Storage

    def get_info(self):#instace Methdo
        print(f"Ram={self.Ram} and Strorage={self.Storage}  {self.Storage_type}")


l1=Laptop("16gb","552gb")
l2=Laptop("8gb","552gb")
l3=Laptop("16gb","5Tb")
l4=Laptop("64gb","1TB")

l3.get_info()


#----------------------------------------------------Classs Method


class Laptop:
    Storage_type="SSD"

    def __init__(self,Ram,Storage):
        self.Ram=Ram
        self.Storage=Storage
    @classmethod
    def get_Storge_type(cls):
        print(f"storage type:{cls.Storage_type}")

    def get_info(self):#instace Methdo
        print(f"Ram={self.Ram} and Strorage={self.Storage}  {self.Storage_type}")


l1=Laptop("16gb","552gb")
l2=Laptop("8gb","552gb")
l3=Laptop("16gb","5Tb")
l4=Laptop("64gb","1TB")

l3.get_Storge_type()
Laptop.get_Storge_type()
print(Laptop.get_Storge_type())



#----------------------------------------------Static Method




class Laptop:
    Storage_type="SSD"

    def __init__(self,Ram,Storage):
        self.Ram=Ram
        self.Storage=Storage

    def get_Storge_type(cls):
        print(f"storage type:{cls.Storage_type}")

    def get_info(self):#instace Methdo
        print(f"Ram={self.Ram} and Strorage={self.Storage}  {self.Storage_type}")

    @staticmethod
    def calc_discount(price,discount):
        Final_price=discount*price/100
        print(f"discount price={Final_price}")
        
l1=Laptop("16gb","552gb")


l1.calc_discount(50_000,500)




#------------------------Pratice_problem--------------------------------


#=>Product Store

#(1).Design And create an Online store for product(name,price)


class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def get_info(self):
        print(f"price of {self.name} is {self.price}")


p1=Product("laptop",45_000)
p2=Product("Mobile",22000)
p3=Product("watch",5000)

p1.get_info()
p3.get_info()
p2.get_info()




#(2) Track Total Products being Created

class Product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1

    def get_info(self):  #instance method
        print(f"price of {self.name} is {self.price}")

    @classmethod           #classs Method
    def total_count(cls):
        print(f"total product in store:{cls.count}")


p1=Product("laptop",45_000)
p2=Product("Mobile",22000)
p3=Product("watch",5000)

p1.get_info()
p3.get_info()
p2.get_info()
Product.total_count()


#(3) Create a static method to calculate discount on each product bassed on a % Parameter



class Product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1

    def get_info(self):  #instance method
        print(f"price of {self.name} is {self.price}")

    @classmethod           #classs Method
    def total_count(cls):
        print(f"total product in store:{cls.count}")

    @staticmethod
    def Dsicount_price(price,Disco):
       print(f"final_price={ price- ( price*Disco/100 ) }")
        


p1=Product("laptop",45_000)
p2=Product("Mobile",22000)
p3=Product("watch",5000)

p1.get_info()
p3.get_info()
p2.get_info()
Product.total_count()
p1.Dsicount_price(50000,3)







        









