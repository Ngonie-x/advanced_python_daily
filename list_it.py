# A list is an ordered collection of items

# the insert method add a new element at any position in the list
# e.g the following inserets the number 100 at index 2 of the numbers list:
numbers = [1, 3, 2, 7, 9, 4]
numbers.insert(2, 100)
print(numbers)

# removing elements from a list
# the del statement allows you to remove elements from a list

del numbers[0]
print(numbers)

# the pop elements removes the last element from a list and returns that element
last = numbers.pop()
print(last)
# you can also use pop with the index of the element you want
second = numbers.pop(1)
print(second)

# to remove an element by value, you can use the remove() method
# for example, the following will remove the element with value 9 from the numbers list

numbers.remove(9)
print(numbers)

#Tuples
# USe tuples when u want to store values that shouldn't change

# Python list sort method
# by default, the sort() method sorts the elements of a list using the 
# less-than(<) operator. It places the lower elements before the higher ones

# to sort from higher to lower, you pass the reverse=True argument to the sort() method


#Examples
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort(reverse=True)
print(guests)

scores = [5, 7, 4, 6, 9, 8]
scores.sort()
print(scores)

# sorting a list of tuples
companies = [
    ('Google', 2019, 134.81),
    ('Apple', 2019, 260.2),
    ('Facebook', 2019, 70.7)
]

# say you want to sort the companies list by revenue from highest to lowest, To do it:
# first, specify a sort key and pass it to the sort() method. To define the sort key, you create a function
# that accepts a tuple and returns the element that you want to sort by:
def sort_key(company):
    return company[2]

companies.sort(key=sort_key, reverse=True)
print(companies)

# or 

companies.sort(key=lambda company: company[2], reverse=True)
print(companies)


# python sorted() function
# to return the new sorted list from the original list, you use the sorted() function, this won't modify the original list

#Examples

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guests = sorted(guests)

print(guests)
print(sorted_guests)

# in reverse order
reverse_guests = sorted(guests, reverse=True)
print(reverse_guests)

scores = [5, 7, 4, 6, 9, 8]
sorted_scores = sorted(scores)
print(sorted_scores)

# list slice
# sub_list = list[begin: end: step]

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

sub_colors = colors[1:4]

print(sub_colors)

# get the n-last elements in a list
sub_last = colors[-3:]
print(sub_last)

# get every 2nd elements in the list
sec2 = colors[::2]
print(sec2)

# using python list slice to reverse a list
reversed_colors = colors[::-1]
print(reversed_colors)

# substitute part of a list
colors[0:2] = ['black', 'white']

print(colors)

# unpacking lists

red, orange, *others = colors
print(red)
print(orange)
print(others)

# using python to iterate over a list with index

# the enumerate() function returns a tuple containing the current index and element of the list

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for item in enumerate(cities):
    print(item)
    
for index, city in enumerate(cities):
    print(f"{index}: {city}")
    
# the enumerate function allows you to specify the starting index
for index, city in enumerate(cities,1):
    print(f"{index}: {city}")
    
result = cities.index('Mumbai')
print(result)



city = 'Osaka'
if city in cities:
    result = cities.index(city)
else:
    print(f"{city} doesn't exist in the list.")
    
# Iterators
# an iterator is the agent that performs the iteration
colors = ['red', 'green', 'blue']
colors_iter = iter(colors)

color = next(colors_iter)
print(color)


## the iterator is stateful. It means that once you consumne an element from the iterator, it's gone
# since u can iterate over an iterator, the iterator is also an iterable object

iterator = iter(colors)
for color in iterator:
    print(color)
    
    
# and a bit of list comprehension
mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

highest_mountains = [m for m in mountains if m[1]> 8600]
print(highest_mountains)