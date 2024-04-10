# 1. Vowel Count
 Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
## Solution:
```
def get_count(sentence): 
    counts = 0
    for vowel in ["a", "e", "i", "o", "u"]:
        counts += sentence.count(vowel)
    return counts
```
    

# 2. String ends with?
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:
```
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
```
## Solution:
```
def solution(text, ending):
    return text.endswith(ending)
```


# 3. Isograms
DESCRIPTION:
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)
"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
```
isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
```

## Solution:
```
def is_isogram(string):
    string = string.upper()
    for char in string:
        if string.count(char) > 1:
            return False
    return True
```

