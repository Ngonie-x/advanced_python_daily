"""Convert words to pig latin
"""


def to_pig_latin(word):
    """converts a word to pig lating equivalent

    Args:
        word (str): the word to be converted
    """

    vowels = ['a', 'e', 'i', 'o', 'u']

    if word[0].lower() not in vowels:
        new_word = word[1:] + word[0] + 'ay'
    else:
        new_word = word + 'way'

    return new_word


print(to_pig_latin('pig'))
print(to_pig_latin("beans"))
print(to_pig_latin("the"))
print(to_pig_latin("end"))
