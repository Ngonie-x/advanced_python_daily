from unicodedata import name


names = ["Alan", "Gregory", "Zlatan", "Jonas", "Tom", "Augustine"]

names.sort(key=lambda x: len(x))
print(names)


numbers = [1, 2, 3, 4, 5]

squared_nums = []


def square(x): return x**2


for n in numbers:
    squared_nums.append(square(n))

print(squared_nums)


# now lets use the map function
num1 = [4, 5, 6]
num2 = [7, 8, 9]

result = map(lambda n1, n2: n1+n2, num1, num2)

print(list(result))

# Filter function
numbers_now = [234, 3245, 639, 550, 654]


even_numbers = list(filter(lambda n: n % 2 == 0, numbers_now))
