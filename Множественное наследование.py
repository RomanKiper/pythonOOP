class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("Init MixinLog")
        self.name =  name
        self.weighit = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weighit}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов.")

class NoteBook(Goods, MixinLog):
    pass


class MobilePhone(Goods, MixinLog):
    pass

n = NoteBook("Acer", 1.5, 1200)
m = MobilePhone("Nokia", 0.15, 2000)
n.print_info()
n.save_sell_log()
m.print_info()
m.save_sell_log()