# TASK 1
 
def get_count(sentence):
    counts = 0
    for vowel in ["a", "e", "i", "o", "u"]:
        counts += sentence.count(vowel)
    return counts

    

# TASK 2

def solution(text, ending):
    return text.endswith(ending)
