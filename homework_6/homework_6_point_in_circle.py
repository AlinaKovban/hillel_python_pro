import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius

    def __contains__(self, point):
        distance = math.sqrt((point.x - self.center.x) ** 2 +
                            (point.y - self.center.y) ** 2)
        if distance <= self.radius:
            return True
        else:
            return False


p1 = Point(1, 2)
c1 = Circle(1, 2, 10)


print(Point(1, 2) in Circle(1, 2, 10))
print(p1 in c1)
