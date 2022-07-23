from collections import defaultdict
from pprint import pprint


def def_value():
    return False


def poor_mans_chart(sentence):
    """Generate the poor mans barchart from the sentence

    Args:
        sentence (str): Sentence to be converted to the poor man's barchart
    """

    # most_used_leters = 'etaoin'
    my_dict = defaultdict(def_value)

    for letter in sentence.replace(" ", ""):
        if my_dict[letter] == False:
            my_dict[letter] = []
        my_dict[letter].append(letter)

    return my_dict


pprint(poor_mans_chart("Here is a little story"))
