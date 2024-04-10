# TASK 1
 Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
# Solution:
def get_count(sentence):
    counts = 0
    for vowel in ["a", "e", "i", "o", "u"]:
        counts += sentence.count(vowel)
    return counts

    

# TASK 2
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
# Solution:
def solution(text, ending):
    return text.endswith(ending)
