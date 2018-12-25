import string

ALPHABET_LOWER = string.ascii_lowercase
ALPHABET_UPPER = string.ascii_uppercase
ALPHABET_ROT13 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
CONSONANT = "bcdfghjklmnpqrstvwxyzß"
DIGITS = string.digits
ESZETT = "ß"
LETTERS = string.ascii_lowercase + string.ascii_uppercase + ESZETT
PUNCTUATION = string.punctuation
SPACE = " "
UMLAUTS = {"ä": "ae", "ö": "oe", "ü": "ue"}
VOWEL = "aeiou"


def alphabetical(s):
    chars = list(s)
    chars.sort()
    return "".join(chars)


def capitalize(s):
    return s.capitalize()


def casefold(s):
    return s.casefold()


def count_multiples(s):
    s = list(s)
    cluster = []
    first_row = [s.pop(0), 1]
    cluster.append(first_row)

    while s:
        char = s.pop(0)
        last_char = cluster[-1][0]
        if char == last_char:
            cluster[-1][1] += 1
        else:
            row = [char, 1]
            cluster.append(row)

    new_string = ""
    for row in cluster:
        char, count = row
        if count > 1:
            new_string += f"{count}{char}"
        else:
            new_string += char

    return new_string


def lower(s):
    return s.lower()


def remove_consonant(s):
    consonant = CONSONANT + upper(CONSONANT)
    table = str.maketrans("", "", consonant)
    return s.translate(table)


def remove_digit(s):
    digits = DIGITS
    table = str.maketrans("", "", digits)
    return s.translate(table)


def remove_letter(s):
    letters = LETTERS
    table = str.maketrans("", "", letters)
    return s.translate(table)


def remove_punctuation(s):
    punctuation = PUNCTUATION
    table = str.maketrans("", "", punctuation)
    return s.translate(table)


def remove_space(s):
    space = SPACE
    table = str.maketrans("", "", space)
    return s.translate(table)


def remove_vowel(s):
    vowel = VOWEL + upper(VOWEL)
    table = str.maketrans("", "", vowel)
    return s.translate(table)


def reverse(s):
    return s[::-1]


def rot13(s):
    alphabet = ALPHABET_UPPER + ALPHABET_LOWER
    alphabet_rot13 = ALPHABET_ROT13
    table = str.maketrans(alphabet, alphabet_rot13)
    return s.translate(table)


def stretch(s):
    s = list(s)
    return " ".join(s)


def swap_pairs(s):
    chars = list(s)
    n = len(chars)
    n = n if n % 2 == 0 else n-1

    for i in range(0, n, 2):
        chars[i], chars[i+1] = chars[i+1], chars[i]

    return "".join(chars)


def swap_umlaut(s):
    for umlaut, replace in UMLAUTS.items():
        s = s.replace(umlaut, replace)
        s = s.replace(upper(umlaut), title(replace))
    return s


def swapcase(s):
    return s.swapcase()


def title(s):
    return s.title()


def upper(s):
    return s.upper()
