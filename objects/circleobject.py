class Circle:

    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad

    def leftKeyPress(self):
        self.x = self.x - 5
        print(self.x)


