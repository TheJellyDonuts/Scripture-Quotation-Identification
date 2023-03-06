import json
import re

# remove all items from a list with a given value 
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def parseGreek(filePath):
    # import file from filepath
    with open(filePath, "r") as f:
        raw_lines = f.readlines()

    # find lines
    
    clauses = []
    for line in raw_lines:
        lineNum, txt = line.split(" ", 1)
        delimiters = []
        for delim in re.finditer("·|.|;", txt):
            delimiters.append(txt[delim.start()])
        lineClauses = re.split("·|.|;", txt)
        for i in range(lineClauses.len):
            
            # find words
            words = lineClauses[i].split(" ")

            # sanitize words
            # TODO: remove greek article adjectives from word list

            clauses.append((lineNum, words, delimiters[i]))
            # NOTE: the clauses have three values
            # clause[0] gives the line num string from the inputted txt file (the two period separated numbers shown at the beginning of a line)
            # clause[1] gives the array to find words in
            # clause[2] gives the punctuation at the end of the clause

    # return json file
    return json.dumps(clauses)

print(parseGreek("./texts/001-i_clement.txt"))