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