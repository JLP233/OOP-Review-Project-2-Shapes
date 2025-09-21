import math

#Basic Shape Class
class BasicShape:
    def __init__(self, name="Shape"):
        self._name = name
        self._area = 0.0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def area(self):
        return self._area



# Circle Shape Class
class Circle(BasicShape):
    def __init__(self, x, y, r, n="Circle"):
        super().__init__(n)
        self._x_center = x
        self._y_center = y
        self._radius = r
        self.calc_area()

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.calc_area()

    def calc_area(self):
        self._area = math.pi * (self._radius ** 2)




