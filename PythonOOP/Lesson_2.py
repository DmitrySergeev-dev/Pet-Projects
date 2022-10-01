# Инициализатор и финализатор
class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        print("call __init__()")
        self.x = x
        self.y = y

    def __del__(self):
        print("Deleting of object" + str(self))

    def set_coords(self, x, y):
        print("call of " + str(self))
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point(5, 6)
# pt.set_coords(1, 2)
print(pt.__dict__)
