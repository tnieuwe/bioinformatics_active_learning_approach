# Insert your HammingDistance function here, along with any subroutines you need
p = "TAAGGATCGATAAATACATATCTCTACATGGCGTAAGCTCATAACACAGATTTCTCGCGTCGTGTAAACCACCACGTTCCCATCACCATGGTAATACAAGTAATGCAAGAGCTCACGAACTAGCATGCCCCGAAGTCCCCGTCCTTTCGTTATATGGCCGGGCGCTGATGGTGTTCACTAATAGCCTACAGACAGACTCAGGAACCAAAAATGACGAGTACGAACCGGGTATCCGACAGTCTAAGCGGGCCGTCATTCGTGCTGTAAGCTGTGAAACGTCGATGATGGAGCGTGTCAGTCGAACAGTAACCTAATGCTTGCATCGTGAGTTACTATTGGTTGGCATGCACTGTCAGATGACGCGGTAATTTCTCATCCGTCAGCCACATATACAACCTACTGCAGACGCCACAAAAGTTACAGATCTCTACATATACGGAATAAACGAAATTCGATACTCCGCCCTTGGGGCTAACTGTACGTGTGCCTAGGCGGTTATCACTCGGCCTTCCTTGACGAGATACCTATCCTAGGTCACCTTAGTTACGCAGAAAGGCTCACATATTCAACCTTCATCAGGGAAATCCGTCGGTACAAGTCGAGTGAACGTGAAGACGCCCCCCCCCATACCTGATTGTCTTTATGCATGCTAGTTAATCGGCGAATTTATTGCACGAGGAGATCTGGCAAAGCATGTTGCCATGTGTTCCTTAACGAATGAGTGAGGACTAAAAGGAGCTTGCGCGTTACCAAAAAACTCGTCCGTGTCAACAACAAGCCAGACTGAGGAGGTGATGCTTGTGTTGTACATGTAACTAAAGCATCGAAAGTACTGGCCTTTCCCTGACCATCGGCAAAGGATACTCTGGGGTAGCAAATTACAGCCCGGGAATGTATAAGGTGACGAAGGTACCGAGAGCACAGGCGGTTCATCACGTTGACCCTATCCATTAAGGCGATACAGTTCGGCGCATGTGCATCGGGCGCGCACTATATCATGAGACCCCTAGAAGTCGATCTGGCCCAGAAAAAAACAAGTTATTCTGGGAAAACATTCTTAATTAGCCATAGTGCCGCTTTTAGTGACTACATACTAGAATACGCATCCGCCCGCTTTGATGACCGACCCACCTTTAATTGCCTCTGGTTACCCATTTATCACCTCGCAAATATTACGA"
q = "GGCCCCTGTAAGAGCTACCGCGTGCGACTCGGCTAAGAAAGCGCTCGCGGCTGTGTCTGTGCTGTTCATGCGATACGATATAGAGATTGGCACCTTTCAGCCAACCGTACGTTTTTCTATACCAAGCACGGTTACACGAAACGGCCTTGGCATTACCCCAAGGGGGCGGCGGCCCGTCCATCTAAAATAGCCTGGCAGAAGGTATCTTGACACGGGAGTAGGGGCTCTACCAGATAGGGCCTAACCCTGAGCCCTTACCAATACAATTTATGTCCTTGAGCTTTTTTGCTGGCCCAGCCTGTGATGCTGGTTTGCTCTTACTTAAGGCGACACGTGTAGGTTGTTGAGACTCCACTTACGTAGCAAGGTACCCAGGCAATTACCTAGTGATTGTCGTGGCCGAAACCGACGTAGATCACATATACTGTAGGACGGTTTAAGAAAGCTGGCAGGCGCGTGTCCCAATTCCTCTTAAATCCATTGCTAACTATCAAATACCGGGAACGGCTAACGCTAGTAGCTTATAATAACACGTACCAAAGACGAATCCGATTATGCCGATATAGCCGCAGCACATTCGTGGACGCACACAAATGGGCGACCGATATAAAGGAGATGTGGAAATTGAGGAGTATTTTCAGCGTCTGACGGAAAGTTATCAGGCTGGAGTCTCATGGTGAATAAAGCAACACAAAAATCTCGGGCACAAAAATTTACTCAATTCTCTCTGCCAGTGGTAGTCGTTCGCTGCAGCGGGTAACCTTATTCATCTCTCTTCATGGTAACGCTGTACATAAATTCTTTGCAACAATAGAAATACAAACCGGATCATAATTACTATTTGGTCTCTGCGAGTGAGAAGAACGCTTACTCTTCTAAATAATACTGCATACCTTGAACTGTCCGATTCTACACGGGAAAACCGTATGGACTCTCCTCCCATAAGCCGATAGGACTTCTGCAATCCATTACTCTTCCGCTCATGGGACATCCAATACGGACCGCAGCGCTGGCTTCAGGTGTTGCTGTCTAGGAATGTGTAATCAAAATACGCTCGCTCATGGAAGAGACTCCATGGATCGTGTAGTCACGAGACAGGCCTCCAAAGATGCGAATTTTTAAGACTCTACTGTATACCTCGTGAGACGTCTTAAAATTGAATGATCAGTTATATGCAC"
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

res = HammingDistance(p,q)
print(res)