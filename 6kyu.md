# 1. Multiples of 3 or 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

## Solution:
```
def solution(number):
    sum = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            sum +=num
    return sum
    if number < 0:
        return 0
```

# 2. Array.diff
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]


## Solution:
```
def array_diff(a, b):
    for presence in b:
      if presence in a:
        for item in range(a.count(presence)):
            a.remove(presence)
    return a
```

# 3. Duplicate Encoder
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

## Solution:
```
def duplicate_encode(word):
    string = word.lower()
    unique = ''
    for char in string:
        if string.count(char) > 1:
            unique += ')'
        else:
            unique += '('
    return unique

print(duplicate_encode('Mabohlale'))

```

