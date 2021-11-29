# lambda expressions allow you to define anonymous functions
# Anonymous functions are functions without names. The anonymous functions are usefule when you need to use them once
# A lambda expression typically contains one or more argumnets, but it can have only one expression

# lambda parameters: expression

# Examples:

def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


def first_last(first_name, last_name):
    return f"{first_name} {last_name}"


def last_first(first_name, last_name):
    return f"{last_name} {first_name}"

full_name = get_full_name('John', 'Doe', first_last)
print(full_name)

full_name = get_full_name('John', 'Doe', last_first)
print(full_name)

# Instead of all the above
fullname = get_full_name('John', 'Doe', lambda first_name, last_name: f"{first_name} {last_name}")
print(fullname)

namefull = get_full_name('John', 'Doe', lambda first_name, last_name: f"{last_name} {first_name}")


def times(n):
    return lambda x: x*n

double = times(2)
print(double)

triple = times(3)

print(triple(2))
print(triple(3))


# python lambda in a loop
callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)
    
for f in callables:
    print(f())