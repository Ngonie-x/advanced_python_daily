characters = set('letters')
print(characters)

skills = {'Python programming', 'Software Design'}

skills.add('Problem Solving')
print(skills)

skills.discard('Software Design')
print(skills)

skill = skills.pop()

# removing all elements from a set
skills.clear()
print(skills)

# to make a set immutable, you use built-in function called frozenset()
skills = {'Programming', 'Software Design', 'Problem Solving'}
skills = frozenset(skills)


for index, skill in enumerate(skills, 1):
    print(f"{index}.{skill}")
    
    
tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = set(map(lambda x: x.lower(), tags))
print(lowercase_tags)


# set union
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s = s1.union(s2)
print(s)


s3 = s1 | s2
print(s3)

# lets pass a set to the union method
rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)
print(ratings)

# set intersection
a1 = {'Python', 'Java', 'C++'}
a2 = {'C#', 'Java', 'C++'}
a = a1.intersection(a2)
print(a)

b = a1 & a2
print(b)


numbers = {1, 2, 3}
scores = [2, 3, 4]

numbers = numbers.intersection(scores)
print(numbers)

# Python set difference
# the difference between two sets results in a new set that has elements from the 
# the first set which aren't in the second set

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.difference(s2)
print(s)

x = s1-s2
print(x)

# Python symmetric difference
# the symmetric difference of two sets is a set of elements that are in either sets but not in their intersection

sd = s1.symmetric_difference(s2)
print(sd)

sd2 = s1 ^ s2
print(sd2)

new_set = numbers.symmetric_difference(scores)
print(new_set)

# subsets
# you can use the issubset() method to check if a set is a subset of another

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(scores.issubset(numbers))# True

# a set is also a subset of itself

# Using subset operators

result = scores <= numbers
print(result)# True

# proper subset
result = scores < numbers
print(result)

result = numbers < numbers
print(result)# False

# is superset

result = numbers.issuperset(scores)
print(result)# True

# A set is also a superset of itself

result = numbers >= scores
print(result)# True

result = numbers > scores
print(result)

# Disjoint set
# two sets are disjoint if they have no elements in common

odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}

result = odd_numbers.isdisjoint(even_numbers)
print(result)# True


letters = {'A', 'B', 'C'}
result = letters.isdisjoint([1, 2, 3])
print(result)