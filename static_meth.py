import abc


class Pizza:
    def __init__(self, ingridients):
        self.ingridients = ingridients

    @staticmethod
    def mix_ingridients(x, y):
        return x+y

    def cook(self):
        return self.mix_ingridients()

    # class method
    @classmethod
    def get_radius(cls):
        return cls.radius

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese(), fridge.get_vegetables())


class BasePizza(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_ingridients(self):
        """Returns the ingridient list"""


class Calzone(BasePizza):
    def get_ingridients(self, with_egg=False):
        egg = Egg() if with_egg else None
        return self.get_ingridients + [egg]
