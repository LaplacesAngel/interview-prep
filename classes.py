class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mySelf(self):
        return f"Hello my name is {self.name} and I'm {self.age} years old"


p1 = Person("John", 38)

print(p1.mySelf())
















class Vehicle:
    def __init__(self, make, model, year = ''):
        self.make = make
        self.model = model
        self.year = year

    def myCar(self):
        if self.year:
            return f"My car is a {self.make} {self.model} and was built in {self.year}"
        else:
            return f"My car is a {self.make} {self.model}"
    

car1 = Vehicle("Honda","Accord", 1996)

print(car1.myCar())















class Animal:
    def __init__(self, name, species, height):
        self. name = name
        self.species = species
        self.height = height

    def myAnmial(self):
        return f"Your animal's name is {self.name} and it is a member of the {self.species} species. It is {self.height} feet tall typically"
    

an1 = Animal("Carl", "Bird", 1)

print(an1.myAnmial())