# suppose you want to double every number in the following list:
bonuses = [100, 200, 300]

# The map() function iterates over all elements in a list (or a tuple), applies a function to each and returns a new iterator of the new elements.
# iterator = map(fn, list)

def double(bonus):
    return bonus * 2

iterator = map(double, bonuses)
print(iterator)

for i in iterator:
    print(i)
    
it = map(lambda bonus: bonus * 2, bonuses)
print(list(it))


# Examples
names = ['david', 'peter', 'jenifer']
new_names = map(lambda name: name.capitalize(), names)
print(list(new_names))


carts = [
    ['SmartPhone', 400],
    ['Tablet', 450],
    ['Laptop', 700]
]

TAX = 0.1
carts = map(lambda item: [item[0], item[1], item[1]*TAX], carts)
print(list(carts))