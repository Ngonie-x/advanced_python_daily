# python reduce function
# reduce(fn, list)

#The reduce() function applies the fn function of two arguments cumulatively to the items of the list, from left to right, to reduce the list into a single value.
#Unlike the map() and filter() functions, the reduce() isn’t a built-in function in Python. In fact, the reduce() function belongs to the functools module.

from functools import reduce

def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} = {a + b}")
    return a+b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)

# or

total = reduce(lambda a, b: a+b, scores)