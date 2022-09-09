from functools import partial
from first import first


def shorten(string_list):
    length = len(string_list[0])
    for s in string_list:
        length = yield s[:length]


mystringlist = ['loremipsum', 'dolorsit', 'ametfoobar']

shortstringlist = shorten(mystringlist)

result = []

try:
    s = next(shortstringlist)
    result.append(s)
    while True:
        number_of_vowels = len(filter(lambda letter: letter in 'aeiou', s))
        # truncate the next string depending on the number of vowels in the previous one
        s = shortstringlist.send(number_of_vowels)
        result.append(s)
except StopIteration:
    pass


# finding the first item using first()
first([0, False, None, [], (), 42])
# 42
first([-1, 0, 1, 2])
# -1
first([-1, 0, 1, 2], key=lambda x: x > 0)
1


# lets learn some functools


def greater_than(number, min=0):
    return number > min


first([-1, 0, 1, 2], key=partial(greater_than, min=42))
