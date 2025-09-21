
class BasicShape:
    def __init__(self, name="Shape"):
        self._name = name
        self._area = 0.0

    def get_name(self):
        return self._name

    def get_area(self):
        return self._area

    def set_name(self, name):
        self._name = name

    def calc_area(self):
        pass

