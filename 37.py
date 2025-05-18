import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius*self.radius
    
    def perimeter(self):
        return 2*math.pi*self.radius
    

c1 = Circle(30)
print(c1.radius)
print(c1.area())
print(c1.perimeter()) 

        