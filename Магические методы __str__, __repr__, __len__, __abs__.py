class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}:{self.name}"

    def __str__(self):
        return f"{self.name}"
# repr служит для вывода отладочной информации, а str информации для пользователя.
cat = Cat("Vasia")


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))

p = Point(1,2,-3,-8)
print(len(p))
print(abs(p))