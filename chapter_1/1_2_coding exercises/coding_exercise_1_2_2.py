## coding_exercise_1_2_1
## The exercise wants me to create a function taking a string input [ATGC] and
## a k that will be the n of characters for the kmers. We will return the most 
## common kmer(s) of the length k in the text.

from typing import Dict, final


text_samples = """CCGCAATGATGCCCAACCCTTCTTGACCGCAATGCCGCAATGCGTGACCTCCGTGACCTCATGCCCAACCCTTCTTGATTGGGACGTTGGGACGTTGGGACGCGTGACCTCCGTGACCTCCCGCAATGCGTGACCTCCGTGACCTCCCGCAATGTTGGGACGCCGCAATGATGCCCAACATGCCCAACCGTGACCTCCCTTCTTGACCTTCTTGATTGGGACGCGTGACCTCCCGCAATGATGCCCAACCGTGACCTCCGTGACCTCATGCCCAACCGTGACCTCCGTGACCTCCGTGACCTCCGTGACCTCCCTTCTTGACGTGACCTCTTGGGACGATGCCCAACCGTGACCTCATGCCCAACATGCCCAACCCGCAATGCCTTCTTGACCTTCTTGACCGCAATGCGTGACCTCCCGCAATGCGTGACCTCTTGGGACGCCGCAATGCGTGACCTCCCTTCTTGACCTTCTTGACCGCAATGTTGGGACGCCTTCTTGATTGGGACGTTGGGACGATGCCCAACTTGGGACGCCTTCTTGACCGCAATGCGTGACCTCCCTTCTTGACCGCAATGCCTTCTTGATTGGGACGCGTGACCTCTTGGGACGCCTTCTTGACGTGACCTCCCGCAATGCCTTCTTGACCGCAATGATGCCCAACCGTGACCTCCCTTCTTGATTGGGACGCGTGACCTCATGCCCAACTTGGGACGCCTTCTTGACCGCAATGTTGGGACGCCGCAATGCCGCAATGATGCCCAACTTGGGACGCGTGACCTCATGCCCAACATGCCCAACTTGGGACGCCTTCTTGATTGGGACGCCGCAATGCGTGACCTC"""
text_samples = text_samples.replace("\n", "")
k_sample = 14

def DictFrequentWords(text, k):
    text_length = len(text)
    window_length = text_length - k
    kmer_dict = dict()
    ## Need to add + 1 to the range to include the last value for some reason?
    for ind in range(0, window_length + 1):
        cur_string =  text[ind:ind + k]
        if cur_string in kmer_dict.keys():
            kmer_dict[cur_string] = kmer_dict[cur_string] + 1
        else:
            kmer_dict[cur_string] = 1
    max_hit = max(kmer_dict.values())
    final_dict = {key: value for key, value in kmer_dict.items() if value == max_hit}
    return(final_dict)

result = DictFrequentWords(text_samples, k_sample)
for key, value in result.items():
    print(key)
