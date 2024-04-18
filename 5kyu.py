"""
1. Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

#Solution

def move_zeros(lst):
    zero_list = list(filter(lambda a: a == 0 and not isinstance(a, bool), lst))
    array = list(filter(lambda a: a != 0 or isinstance(a, bool), lst)) + zero_list
    return array
