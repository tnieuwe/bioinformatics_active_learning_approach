from typing_extensions import Annotated


pattern = "ATAT"
genome = "GATATATGCATATACTT" 
f = open("test_file_exercise_1_3_1.txt")
pattern = f.readline()
genome = f.readline()

def PatternMatch(pattern, genome):
    ## Using the brute force method of pattern recognition
    pattern_len = len(pattern)
    pattern_loc = list()
    for ind in range(0, len(genome) - pattern_len + 1):
        if genome[ind] == pattern[0]:
            if genome[ind:ind+pattern_len] == pattern:
                pattern_loc.append(ind)
    return(pattern_loc)
    
            
PatternMatch(pattern, genome)    
        

## Unit tests... kinda
## For interactive
## os.chdir("C:/Users/Tim/Documents/Python Scripts/bioinformatics_active_learning/bioinformatics_active_learning_approach/chapter_1/1_3_coding_exercises/")
for test_ind in range(1,6):
    f = open("PatternMatching/inputs/input_" + str(test_ind) + ".txt")
    pattern = f.readline().strip()
    genome = f.readline().strip()
    f2 = open("PatternMatching/outputs/output_" + str(test_ind) + ".txt")
    correct_output = f2.readline().strip()
    result = PatternMatch(pattern, genome)
    if ' '.join(map(str, result)) == correct_output:
        print("Test ", test_ind, " is succesful")
    else:
        print("Test ", test_ind, " is failed")
    f.close()
    f2.close()

f = open("dataset_240215_5.txt")
pattern = f.readline().strip()
genome = f.readline().strip()
f.close()
result = PatternMatch(pattern, genome)
r = open("1_3_2_output.txt", "w")
r.write(' '.join(map(str, result)))
r.close()


## Exercise break
f = open("Vibrio_cholerae.txt")
pattern = "CTTGATCAT" 
genome = f.readline().strip()
f.close()
result = PatternMatch(pattern, genome)
r = open("vibrio_output.txt", "w")
r.write(' '.join(map(str, result)))
r.close()