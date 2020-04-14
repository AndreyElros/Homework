#Задание 2
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return int((self._length * self._width * self.vol * self.ons) / 1000)

class MassCount(Road):
    def __init__(self, _length, _width, vol, ons):
        super().__init__(_length, _width)
        self.vol = vol
        self.ons = ons

r = MassCount(20, 5000, 25, 5)
print(r.mass(), 'т')