class Geom:
    def get_pr(self):
        raise NotImplementedError("В дочернем классе должен быть переопределен мето get_pr()")

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return self.w * 2 + self.h * 2

class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return self.a * 4

class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c

geom = [Rectangle(1,2), Rectangle(3,4),
        Triangle(2,3,4), Triangle(5,6,7),
        Square(5), Square(8)]
for i in geom:
    print(i.get_pr(), i.__class__)