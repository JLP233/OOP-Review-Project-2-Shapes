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
    def __init__(self, a, b, r, n="Circle"):
        super().__init__(n)
        self._center_A_coordinate = a
        self._center_B_coordinate = b
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



# Rectangle Shape Class
class Rectangle(BasicShape):
    def __init__(self, l, w, n="Rectangle"):
        super().__init__(n)
        self._length = l
        self._width = w
        self.calc_area()

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, l):
        self._length = l
        self.calc_area()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w
        self.calc_area()

    def calc_area(self):
        self._area = self._length * self._width



# Square Shape Class
class Square(BasicShape):
    def __init__(self, s, n="Square"):
        super().__init__(n)
        self._side = s
        self.calc_area()

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, s):
        self._side = s
        self.calc_area()

    def calc_area(self):
        self._area = self._side * self._side

