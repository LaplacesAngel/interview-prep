#write a python function that takes in roman numerals and returns them as a regular python integer
#underscore is better than camelcase

#how many prompts should it be able to take?

#works for addition for now at least

def roms_to_ints(prompt):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "C": 100,
        "M": 1000
    }

    total = 0

    for char in prompt:
        total += roman_dict[char]
    
    print(total)


roms_to_ints("III")


#floored qution, will round down
print(89//3.21, 5**2)



text = "hi there paul"
print(text.split()[0])




#casting
x = 1.0
y = 2.8
z = "3"

print(str(x) + str(y))


#Classes
class MyClass:
    x = 5
    y = 100



class MyNewClass:
    def MyFunction(self, arg):
        return 1 + arg


ob1 = MyClass()
ob2 = MyNewClass()
print(ob2.MyFunction(1))


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)



















class Vehicle():
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        

car1 = Vehicle("honda", "accord")

print(car1.make)



















class Car(Vehicle):
    def __init__(self, make, model, wheels = "unknown") -> None:
        super().__init__(make, model)
        self.wheels = wheels
        


maserati = Car("Maserati", "Ventador", 5)

print(maserati.make, "\n", maserati.wheels)








# romansAndarabics = {"I":1, 
# "II": 2,
# "III" :3,
# "IV" :4, 
# "V" :5,
# "X" :10,
# "L" :50,
# "C" :100,
# "D ":500,
# "M" :1000}


# def romanNumtoInt(roman):
#     total = 0
#     for char in roman:
#         total += romansAndarabics[char]
    
#     return total

# print(romanNumtoInt("IX"))