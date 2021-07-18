## 1.2 Coding exercise 1
test_text = "GCGCG"
test_pattern = "GCG"

def PatternCount(text, pattern):
    """This is a redundant piece of code for the string method.count()"""
    count = 0
    pattern_length = len(pattern)
    difference = len(text) - pattern_length
    for ind in range(0, difference):
        if text[0:0+pattern_length] == pattern:
            count = count + 1
    return(count)


