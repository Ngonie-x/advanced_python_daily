class UpperCaseMeta(type):
    def __new__(cls, name, bases, attrs):
        uppercase_attrs = {
            attr if attr.startswith("__") else attr.upper(): value
            for attr, value in attrs.items()
        }
        return super().__new__(cls, name, bases, uppercase_attrs)


class MyClass(metaclass=UpperCaseMeta):
    var1 = "value1"

    def my_method(self):
        return "This is a method in MyClass"
