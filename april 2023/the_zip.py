# Learning about the zip function

fruits = ['apple', 'banana', 'orange']
prices = [1.2, 0.9, 1.5]


for fruit, price in zip(fruits, prices):
    print(fruit, price)


fruit_prices = list(zip(fruits, prices))
print(fruit_prices)


names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(name, age)
