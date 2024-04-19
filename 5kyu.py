"""
1. Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

#Solution

def move_zeros(lst):
    return [x for x in lst if x != 0] + [0] * lst.count(0)


"""
2.First non-repeating character

Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.
"""

#Solution

def first_non_repeating_letter(string):
    for char in string:
        if string.lower().count(char.lower()) == 1:
            return char
    return ""


"""
3. RGB To Hex Conversion

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""

#Solution

def rgb(r, g, b):
    return convert_to_rgb(r) + convert_to_rgb(g) + convert_to_rgb(b)

def convert_to_rgb(rgb_val):
    if rgb_val <= 0:
        return '00'
    elif rgb_val >= 255:
        return 'FF'
    else:
        first_hex = int(rgb_val // 16)
        second_hex = int((rgb_val / 16 - first_hex) * 16)
        return get_hex_value(first_hex) + get_hex_value(second_hex)

def get_hex_value(digit):
    rgb_to_hex = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
    }
    return rgb_to_hex[str(digit)]


