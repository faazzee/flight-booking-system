class shape:
    def area():
        return None

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.radius**2
    
radius=int(input("g"))
Circle=circle(radius)
print(Circle.area())