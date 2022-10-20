class Geom:
    name = "Geom"

    def __init__(self, x1, x2, y1, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):
    def drow(self):
        print("Рисование линий")


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        super().__init__(x1, x2, y1, y2,)
        print(f"Инициализатор Rect {self.__class__}")
        self.fill = fill

    def drow(self):
        print("Рисование прямоугольника")

l = Line(0, 0, 10 ,20)
r = Rect(10,12,20,22)
print(r.__dict__)
