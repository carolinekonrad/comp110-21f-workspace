"""Practice with dictionaries."""

__author__ = "730369129"

def invert(xs: dict[str, str]) -> dict[str, str]:
    inverse_list: dict[str, str]
    inverse_list = dict()
    is_new_value_present: bool = False
    for key in xs:
        is_new_value_present = xs[key] in inverse_list
        if is_new_value_present == True:
            raise KeyError("That key is already in the new dictionary!")
        inverse_list[xs[key]] = key
    return inverse_list

def favorite_color(xs: dict[str, str]) -> str:
    color_list: dict[str, int]
    color_list = dict()
    winner: int = 0
    final: str = ""
    new_color_present: bool = False 
    for key in xs:
        new_color_present = xs[key] in color_list
        if new_color_present == True:
            color_list[xs[key]] += 1
        else:
            color_list[xs[key]] = 1
    for value in color_list:
        if color_list[value] > winner:
            winner = color_list[value]
            final = value
    return final


def count(xs: list[str]) -> dict[str, int]:
    dict_counts: dict[str, int]
    dict_counts = dict()
    new_word_present: bool = False 
    for key in xs:
        new_word_present = key in dict_counts
        if new_word_present == True:
            dict_counts[key] += 1
        else:
            dict_counts[key] = 1
    return dict_counts