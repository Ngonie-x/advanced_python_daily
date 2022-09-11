# A decorator is a function that takes another function as an argument
# and replaces it with a new, modified function.

import functools
import uuid
from logging import raiseExceptions


def identity(f):
    return f


@identity
def foo():
    return 'bar'


_functions = {}


def register(f):
    global _functions
    _functions[f.__name__] = f
    return f


@register
def foo():
    return 'bar'


def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get or put food")
        return f(*args, **kwargs)
    return wrapper

# stacking decorators


def check_user_is_not(username):
    def user_check_decorator(f):
        def wrapper(*args, **kwargs):
            if kwargs.get('username') == username:

                raise Exception("This user is not allowed to get food")
            return f(*args, **kwargs)

        return wrapper

    return user_check_decorator


class Store(object):
    @check_is_admin
    @check_user_is_not('user123')
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        self.storage.put(food)


# writing class decorators


def set_class_name_and_id(klass):
    klass.name = str(klass)
    klass.random_id = uuid.uuid4()
    return klass


@set_class_name_and_id
class SomeClass(object):
    pass


class CountCalls(object):
    def __init__(self, f):
        self.f = f
        self.called = 0

    def __call__(self, *args, **kwargs):
        self.called += 1
        return self.f(*args, **kwargs)


@CountCalls
def print_hello():
    print("hello")

# a decorator replaces the original function with a new one built on the fly
# However, this new function lacks many of the attributes of the original function,
# such as its docstring and its name
# this problem can be fixed using functools


def foobar(username="someone"):
    """Do crazy stuff"""
    pass


foobar = functools.update_wrapper(check_is_admin, foobar)
