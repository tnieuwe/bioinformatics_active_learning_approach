## Approximate pattern match
import os
Pattern = "CCA"
Text = "CCACCT"
d = 0
## Going to use the hamming distance code from earlier
def HammingDistance(p: str, q: str) -> int:
    shared_length = len(p)
    hamming_dist = 0
    for nucleotide in range(0, shared_length):
        if  q[nucleotide] != p[nucleotide]:
            hamming_dist += 1
        else:
            continue
    return(hamming_dist)
    pass


def ApproximatePatternMatching(Pattern: str, Text: str, d: int):
    ## We're going to create a sliding window that slides along Text
    ## testing if the hammign distance is less than d
    pattern_length = len(Pattern)
    index = 0
    starting_points = list()
    max_index = len(Text)
    ## Without the +1 it is not checking the furthest most right side
    ## this is likely why I failed the first time
    for start in range(0, max_index - pattern_length + 1):
        cur_hamm = HammingDistance(Pattern, Text[start:start+pattern_length])
        if cur_hamm <= d:
            starting_points.append(str(start))
        else:
            continue
    return(starting_points)
    pass

res = ApproximatePatternMatching(Pattern, Text, d)
print(*res, " ")

print(os.getcwd())
## Read in data 
with open("C:/Users/timni/OneDrive/Documents/tim_old_documents/Python Scripts/bioinformatics_active_learning/bioinformatics_active_learning_approach/chapter_1/1_8_coding_exercises/ApproximatePatternMatch_final.txt") as file:
    lines = [line.rstrip() for line in file]

res = ApproximatePatternMatching(lines[0], lines[1], int(lines[2]))
f = open("C:/Users/timni/OneDrive/Documents/tim_old_documents/Python Scripts/bioinformatics_active_learning/bioinformatics_active_learning_approach/chapter_1/1_8_coding_exercises/ApproximatePatternMatch_out.txt", "w")
f.write(" ".join(res))
f.close()