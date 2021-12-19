import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(figure1, figure2):
        """Calculates distance between centers of 2 given figures"""
        x1, y1 = figure1.get_center()
        x2, y2 = figure2.get_center()
        x_diff = abs(x1 - x2)
        y_diff = abs(y1 - y2)
        return math.sqrt(x_diff ** 2 + y_diff ** 2)


class Circle(Shape):
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        super().__init__(x, y)

    def get_center(self):
        """Returns the center of figure"""
        return self.x, self.y

    def get_area(self):
        """Returns the area of figure"""
        return math.pi * self.radius ** 2

    def move(self, x, y):
        """Changes geometrical center of figure to given coordinates"""
        self.x = x
        self.y = y


class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    def get_center(self):
        """Returns the center of figure"""
        return self.x, self.y

    def get_vertex(self):
        """Returns the vertices of figure"""
        vertices = [
            (self.x - self.side / 2, self.y - self.side / 2),
            (self.x - self.side / 2, self.y + self.side / 2),
            (self.x + self.side / 2, self.y - self.side / 2),
            (self.x + self.side / 2, self.y + self.side / 2)
        ]
        return vertices

    def get_area(self):
        """Returns the area of figure"""
        return self.side ** 2

    def move(self, x, y):
        """Changes geometrical center of figure to given coordinates"""
        self.x = x
        self.y = y


class Triangle(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    def get_center(self):
        """Returns the center of figure"""
        return self.x, self.y

    def get_vertex(self):
        """Returns the vertices of figure"""
        vertices = [
            (self.x, self.y + self.side / math.sqrt(3)),
            (self.x - self.side / 2, self.y - self.side * math.sqrt(3) / 6),
            (self.x + self.side / 2, self.y - self.side * math.sqrt(3) / 6),
        ]
        return vertices

    def get_area(self):
        """Returns the area of figure"""
        return self.side ** 2 * math.sqrt(3) / 4

    def move(self, x, y):
        """Changes geometrical center of figure to given coordinates"""
        self.x = x
        self.y = y


# Examples
circle = Circle(10)
print("The default center of circle: ", circle.get_center())
print("The radius of circle: ", circle.radius)
print("The area of circle: ", circle.get_area())
# Changes radius of circle
circle.radius = 100
print("The new radius of circle: ", circle.radius)
print("The new area of circle: ", circle.get_area())
# Checks that the center has not changed
print("The center of circle: ", circle.get_center())

square = Square(x=25, y=50)
print("\nThe default side of square: ", square.side)
print("The user-defined center of square: ", square.get_center())
# Changes size of square
square.side = 15
print("The new side of square: ", square.side)
# Moves figure to coordinates (50, 25) and check new center
square.move(175, 215)
print("The center of square after movement: ", square.get_center())
print("The area of square: ", square.get_area())
print("The list of square vertices:", square.get_vertex())

triangle = Triangle(20, 10, 10)
print("\nThe user-defined center of triangle: ", triangle.get_center())
# Moves figure to coordinates (40, 40) and check new center
triangle.move(40, 40)
print("The center of triangle after movement: ", triangle.get_center())
print("The side of triangle: ", triangle.side)
print("The area of triangle: ", triangle.get_area())
print("The list of triangle vertices:", triangle.get_vertex())
# Changes size of triangle and check new area and vertices
triangle.side = 35
print("The new area of triangle: ", triangle.get_area())
print("The new list of triangle vertices after size changing:", triangle.get_vertex())

# Calculates distance between centers of 2 figures
print("\nThe distance between square and triangle:", Shape.get_distance(square, triangle))
print("The distance between square and circle:", Shape.get_distance(square, circle))
print("The distance between triangle and circle:", Shape.get_distance(triangle, circle))
