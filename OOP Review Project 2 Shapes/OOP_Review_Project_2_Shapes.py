
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


