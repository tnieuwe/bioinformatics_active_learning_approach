Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4 
d = 1

Pattern = "CCACCTCCAGAG"
d = 3
## Get hamming distance function
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


## Must define neighbors function
def Neighbors(Pattern : str, d : int):
    all_nuc = ["A", "C", "T", "G"]
    neighborhood = list()
    neighborhood.append(Pattern)
    for ind in range(0, len(Pattern)):
        cur_nuc = Pattern[ind]
        for rep_nuc in all_nuc:
            if cur_nuc == rep_nuc:
                continue
            neighbor = Pattern[:ind] + rep_nuc + Pattern[ind+1:]
            hamm_dist = HammingDistance(Pattern, neighbor)
            if hamm_dist <= d:
                neighborhood.append(neighbor)
    return(neighborhood)

res = Neighbors(Pattern, d)
print(*res, " ")





#def FrequentistWordswithMismatches(Text: str, k : int, d : int):
#    patterns = list()
#    freqmap = list()
#    text_length = len(Text)
#    for ind in range(0, text_length - k):
#        cur_pattern = Text[ind:ind+k]