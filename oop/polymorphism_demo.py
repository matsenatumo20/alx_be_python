import math

class Shape:
    def area(self):
        raise NotImplementedError("Derived classes need to override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Example usage
def calculate_area(shape: Shape):
    return shape.area()

rectangle = Rectangle(4, 5)
circle = Circle(3)

print(f"Rectangle area: {calculate_area(rectangle)}")
print(f"Circle area: {calculate_area(circle)}")
