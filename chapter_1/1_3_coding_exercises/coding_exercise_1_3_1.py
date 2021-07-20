f = open("test_file_exercise_1_3_1.txt")
test_text = f.readline()

def ReverseComplement(strand):
    rev_strand = strand[::-1].lower()
    nuc_tides = ["A", "C", "T", "G"]
    comp_tides = ["T", "G", "A", "C"]
    for nuc_ind in range(4):
        rev_strand = rev_strand.replace(nuc_tides[nuc_ind].lower(), comp_tides[nuc_ind])
    return(rev_strand)

ReverseComplement(test_text)
## Test 2
ReverseComplement("ACACAC")

## Final answer 
f2 = open("final_1_3_1.txt")
final_text = f2.readline()
data_out = ReverseComplement(final_text)