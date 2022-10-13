class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("bool")
        return self.x == self.y

p = Point(4,4)

if p:
    print("обьект Р дает True")
else:
    print("обьект Р дает False")

