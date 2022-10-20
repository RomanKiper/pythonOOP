class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    __slots__ = ('x', 'y') # в обьектах класса могут присутсвовать только локальные свойсва с указанными именами.
    MAX_coord = 100
    def __init__(self, x, y):
        self.x = x
        self.y = y


p2 = Point2D
print(p2.MAX_coord)

p = Point(1,2)
print(p.__dict__)
print(p.__sizeof__()+ p.__dict__.__sizeof__())