# class Point2D:
#     __slots__ = ("x", "y", "__lenght")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.__lenght = (x * x + y * y) ** 0.5
#
#     @property
#     def lenght(self):
#         return self.__lenght
#
#     @lenght.setter
#     def lenght(self, value):
#         self.__lenght = value


class Point2D:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p = Point3D(10, 20)
p.z = 30
