## Define FrequentWords as it will help in FindClumps

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

text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
kmer = 5
Length = 50 
times =  4
import os
def FindClumps(text, kmer, Length, times):
    found_clumps = list()
    total_length = len(text)
    unique_clumps = list()
    ## Always add 1 to range
    for string_ind in range(0,(total_length - Length + 1)):
        cur_text = text[string_ind: Length + string_ind]
        clump_dict = DictFrequentWords(cur_text, kmer)
        for key, val in clump_dict.items():
            if val >= times:
                found_clumps.append(key)
    for clump in found_clumps:
        if clump in unique_clumps:
            continue
        else:
            unique_clumps.append(clump)
    return(" ".join(unique_clumps))

for test_ind in range(1,6):
    f = open("ClumpFinding/inputs/input_" + str(test_ind) + ".txt")
    text = f.readline().strip()
    variable_line = f.readline().strip()
    kmer, Length, times = map(int, variable_line.split())
    f2 = open("ClumpFinding/outputs/output_" + str(test_ind) + ".txt")
    correct_output = f2.readline().strip()
    result = FindClumps(text, kmer, Length, times)
    if result == correct_output:
        print("Test ", test_ind, " is succesful")
    else:
        print("Test ", test_ind, " is failed")
    f.close()
    f2.close()



f = open("dataset_240217_5.txt")
text = f.readline().strip()
variable_line = f.readline().strip()
kmer, Length, times = map(int, variable_line.split())
result = FindClumps(text, kmer, Length, times)
r = open("ClumpFinder_output.txt", "w")
r.write(' '.join(map(str, result)))
r.close()

## Ecoli test is currently to large for my code, 
## I could make it more efficient in the future
f = open("E_coli.txt")
text = f.readline().strip()
f.close()
result = FindClumps(text, 9, 500, 3)
r = open("ecoli_result.txt", "w")
r.write(' '.join(map(str, result)))
r.close()