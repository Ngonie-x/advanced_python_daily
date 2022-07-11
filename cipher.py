def rot13(message):
    new_string = ''
    for letter in message:
        if check_letter_index(letter) != False:
            new_string += check_letter_index(letter)
        else:
            new_string += letter
    return new_string


def check_letter_index(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    try:
        letter_index = alphabet.index(letter)
        if letter_index > 12:
            letter_index = abs(13-letter_index)
        else:
            letter_index += 13
        return alphabet[letter_index]
    except ValueError:
        try:
            letter_index = alphabet.upper().index(letter)
            if letter_index > 12:
                letter_index = abs(13-letter_index)
            else:
                letter_index += 13
            return alphabet.upper()[letter_index]
        except ValueError:
            return False


print(rot13('Test'))
