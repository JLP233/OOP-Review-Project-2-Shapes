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
class Square(Rectangle):
    def __init__(self, s, n="Square"):
        self._side = s
        super().__init__(s, s, n)
        self.name = n

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, s):
        self._side = s
        self._length = s
        self._width = s
        self.calc_area()



# Program Test
shapes = [
    Rectangle(10, 20, "Rectangle_1"),
    Rectangle(20, 30, "Rectangle_2"),
    Circle(0, 0, 4, "Circle_1"),
    Circle(2, 2, 9, "Circle_2"),
    Square(10, "Square")
]

print("Polymorphism check")
for s in shapes:
    print(s.name, "Area =", s.area)

print("\n Getter/setter check")

