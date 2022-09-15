import collections
import dis


def has_invalid_fields(fields):
    return bool(set(fields) - set(['foo', 'bar']))


def add_animal_in_family(species, animal, family):
    species[family].add(animal)


species = collections.defaultdict(set)
add_animal_in_family(species, 'cat', 'felidea')


# Lets count the number of distinct items in an iterable
c = collections.Counter("Premature optimization is the root of all evil.")
c['P']  # returns the number of occurences of the letter 'p'

c.most_common(2)  # returns the most common two letters


abc = ('a', 'b', 'c')


def concat_a_1():
    for letter in abc:
        abc[0] + letter


def concat_a_2():
    a = abc[0]
    for letter in abc:
        a + letter
