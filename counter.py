from collections import Counter
# counter works with iterable objects


new_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'b', 'b', 'a', 'c', 'b']

print(Counter(new_list))

# counter with string
new_string = 'welcome to advanced foundations'
print(Counter(new_string))

# Counter with dict

new_dict = {'a': 1, 'b': 2, 'c':3, 'd': 4}
print(Counter(new_dict))

# counter with tuple
new_tuple = ('apple', 'banana', 'cherry', 'apple', 'banana', 'fig', 'cherry')

# empty Counter
_counting = Counter()
_counting.update("Hi, python is fun!")
print(_counting)

#delete from Counter
new_dict = {'a': 1, 'b': 2, 'c':3, 'd': 4}
del new_dict['d']
print(Counter(new_dict))