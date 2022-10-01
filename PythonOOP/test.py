class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f"{good.name}: {good.price}" for good in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('tv_1', 1000))
cart.add(TV('tv_2', 500))
cart.add(Table('table', 20))
cart.add(Notebook('notebook_1', 300))
cart.add(Notebook('notebook_2', 450))
cart.add(Cup('cup', 5))


print(cart.get_list())