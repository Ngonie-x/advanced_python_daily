from traceback import print_tb
from turtle import ycor


def even_gen(max):
    n = 2
    while n <= max:
        yield n
        n += 2


def gen_fibonacci():
    n1 = 0
    n2 = 1

    while True:
        yield n1
        n1, n2 = n2, n1+n2


seq = gen_fibonacci()

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
