# class Geom:
#     pass
#
# class Line(Geom):
#     pass
#
# g = Geom()
# l = Line()
#
# print(issubclass(Line, Geom))
# print(isinstance(Line, object))


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))

v = Vector([1,2,3,])
print(type(v), v,)

