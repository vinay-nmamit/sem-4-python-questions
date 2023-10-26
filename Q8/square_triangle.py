class square:
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side * self.side

class triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h
        
    def area(self):
        return 0.5 * self.b * self.h


def findArea(shapeType):
    return shapeType.area()


sq = square(10) #pass any value
tri = triangle(5.5,7.5) #pass any value
print("Area of square:", findArea(sq))
print("Area of triangle:", findArea(tri))
