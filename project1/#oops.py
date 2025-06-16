"""class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

car1=car("maruti suzuki","ciaz",2005)
print(car1.make)"""
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=4*math.pi*(self.radius)**2
        return f"area is {a}"
    def circumference(self):
        c=2*math.pi*(self.radius)
        print(c)

circle=Circle(7)
print(circle.area())
print(circle.circumference())

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return self.name,self.age
person1=person("anjali",40)
print(person1.display())

class employee(person):
    def __init__(self, name, age,sallary):
        super().__init__(name,age)
        self.sallary=sallary
    def display_employee(self):
        return self.sallary,self
person2=employee("aam",34,90000)
print(person2.display())
print(person2.display_employee())

print(employee.mro())

