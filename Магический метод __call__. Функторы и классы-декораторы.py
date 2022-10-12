# class Counter:
#     def __init__(self):\
#         self.__counter = 0
#
#     def __call__(self, step =1,  *args, **kwargs):
#         print("__call__")
#         self.__counter += step
#         return self.__counter
#
# c = Counter()
# c2 = Counter()
# c(5)
# c(2)
# c(3)
# c2()
# c2()
# res = c(3)
# res2 = c2(8)
# print(res, res2)


class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')

        return args[0].strip(self.__chars)


s1 = StripChars('?:!;.> ')
s2 = StripChars(" ")
res = s1("Python is the best language in the world>!!!")
res2 = s2("hello world    !!")
print(res, res2, sep="\n")



