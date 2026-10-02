# Encapsulation = Data + Methods wrapping in one single classs


#DATA HIdnig

class Bank:
    def __init__(self, name, account_no, balance):
        self.name = name          # Public
        self._account_no = account_no  # Protected
        self.__balance = balance  # Private

    def Get_info(self):
        print(self.name)
        print(self._account_no)
        print(self.__balance)


b = Bank("Shivam", 12345, 5000)

print(b.name)          # Public
print(b._account_no)  # Protected
b.Get_info()              # Private data through method


# getter And Setter

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # Getter → value ko read karne ke liye
    def get_balance(self):
        return self.__balance

    # Setter → value ko change/update karne ke liye
    def set_balance(self, balance):
        self.__balance = balance


b = Bank("Shivam", 5000)

print(b.get_balance())   # Getter

b.set_balance(7000)      # Setter

print(b.get_balance())



#inheritance

class Father:
    def house(self):
        print("Father has a house")


class Son(Father):       # Son inherits Father
    def bike(self):
        print("Son has a bike")


s = Son()

s.house()   # Parent ka method
s.bike()    # Child ka method


# #--types of Inheritance
# Single Inheritance → 1 Parent → 1 Child
# Multiple Inheritance → 2+ Parents → 1 Child
# Multilevel Inheritance → Grandparent → Parent → Child



#(1)Single

class Father:
    def house(self):
        print("Father has a house")


class Son(Father):
    def bike(self):
        print("Son has a bike")


s = Son()

s.house()
s.bike()


#(2)Multiple


class Father:
    def house(self):
        print("Father has a house")


class Mother:
    def car(self):
        print("Mother has a car")


class Son(Father, Mother):
    def bike(self):
        print("Son has a bike")


s = Son()

s.house()   # Father se
s.car()     # Mother se
s.bike()    # Son ka own method


#(3)Multilevel


class Grandfather:
    def land(self):
        print("Grandfather has land")


class Father(Grandfather):
    def house(self):
        print("Father has a house")


class Son(Father):
    def bike(self):
        print("Son has a bike")


s = Son()

s.land()    # Grandfather ka method
s.house()   # Father ka method
s.bike()    # Son ka method



#############----SUPER FUNCTION USE---------

class Father:
    def show(self):
        print("Father")


class Son(Father):
    def show(self):
        super().show()   # Parent ka method
        print("Son")


s = Son()
s.show()





#Abstraction



from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def withdraw(self):
        pass


class SBI(Bank):

    def withdraw(self):
        print("Money withdrawn")


s = SBI()
s.withdraw()



#Polymorphism

# same method name → different behavior = Polymorphism.


class Dog:
    def sound(self):
        print("Dog says: Woof")


class Cat:
    def sound(self):
        print("Cat says: Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()

#=>1 Function Overriding

class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog says Woof")


d = Dog()
d.sound()


#=> Ducking Typing

class Dog:
    def sound(self):
        print("Woof")


class Cat:
    def sound(self):
        print("Meow")


def animal_sound(animal):
    animal.sound()


d = Dog()
c = Cat()

animal_sound(d)
animal_sound(c)

