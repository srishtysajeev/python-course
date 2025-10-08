class A: 
    pass

class Point(A): 
    """Description of Point"""
    count = 0
    def __init__(self, x0, y0, name):
        Point.count += 1 # need to put Point to 
        self.x = x0
        self.y = y0
        self.name = name
    def moveBy(self, dx, dy): 
        self.__dict__['x'] += dx 
        self.x += dx
        self.y += dy 
    def __str__(self):
        return f"{self.name} is {self.x} {self.y}"

p1 = Point(100, 200, "point-p1") # this is a pointer and it is creating some dunder variables 
p2 = Point(140, 300, "point-p2")
p3 = Point(240, 330, "point-p3")

print("Count: ", Point.count)
print(p3.count)
print(Point.__dict__)
print(Point.__bases__)
print(p1.__dict__)
print(dir(object))
p1.moveBy(10, 10)
Point.moveBy(p1, 10, 10 )
#print(Print.count)

del p3.x
print(p3.__dict__)
pass 
print(p1)