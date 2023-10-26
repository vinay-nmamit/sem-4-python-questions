#create class circle and finout area and perimeter
import math

class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius

n = int(input("enter the radius: "))
p = circle(n)
print("area : ",p.area())
print("perimeter: ",p.perimeter())
