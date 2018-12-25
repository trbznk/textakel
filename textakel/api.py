from . import textakel

FUNCTIONS = {
    "alphabetical": textakel.alphabetical,
    "capitalize": textakel.capitalize,
    "casefold": textakel.casefold,
    "count_multiples": textakel.count_multiples,
    "lower": textakel.lower,
    "remove-consonant": textakel.remove_consonant,
    "remove-digit": textakel.remove_digit,
    "remove-letter": textakel.remove_letter,
    "remove-punctuation": textakel.remove_punctuation,
    "remove-space": textakel.remove_space,
    "remove-vowel": textakel.remove_vowel,
    "reverse": textakel.reverse,
    "rot13": textakel.rot13,
    "stretch": textakel.stretch,
    "swap-pairs": textakel.swap_pairs,
    "swap-umlaut": textakel.swap_umlaut,
    "swapcase": textakel.swapcase,
    "title": textakel.title,
    "upper": textakel.upper
}


def get_function(name):
    return FUNCTIONS[name]


def get_functions():
    return list(FUNCTIONS.keys())


def takel(function_name, s):
    function = get_function(function_name)
    return function(s)
