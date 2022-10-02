class Point:
    Max_coord = 100
    Min_coord = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.Min_coord <= x <= self.Max_coord:
            self.x = x
            self.y = y
    # @classmethod
    # def set_bound(cls, left):
    #     cls.Min_coord = left

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("доступ запрещен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError("недопустимое имя атребута")
        else:
            return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("__delattr__ вызов метода" + item)
        object.__delattr__(self, item)

pt = Point(1, 2)
pt2 = Point(1, 5)
print(pt.yy)
del pt.x
print(pt.__dict__)
