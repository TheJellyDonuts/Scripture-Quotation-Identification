import json
import re

# remove all items from a list with a given value 
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def parseGreek(filePath):
    # import file from filepath
    with open(filePath, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    # find lines
    
    clauses = []
    for line in raw_lines:
        lineNum, txt = line.split(" ", 1)
        delimiters = []
        for delim in re.finditer("·|\.|\;", txt):
            delimiters.append(txt[delim.start()])
        lineClauses = re.split("·|\.|\;", txt)

        for i in range(len(lineClauses) - 1):
            
            # find words
            words = lineClauses[i].split(" ")

            # sanitize words
            words = remove_values_from_list(words, "ο")
            words = remove_values_from_list(words, "του")
            words = remove_values_from_list(words, "το")
            words = remove_values_from_list(words, "τον")
            words = remove_values_from_list(words, "την")
            words = remove_values_from_list(words, "η")
            words = remove_values_from_list(words, "τω")
            words = remove_values_from_list(words, "τησ")
            words = remove_values_from_list(words, "των")
            words = remove_values_from_list(words, "οι")
            words = remove_values_from_list(words, "τη")
            words = remove_values_from_list(words, "τα")
            words = remove_values_from_list(words, "τουσ")
            words = remove_values_from_list(words, "τοισ")
            words = remove_values_from_list(words, "τασ")
            words = remove_values_from_list(words, "ταισ")
            words = remove_values_from_list(words, "αι")
            words = remove_values_from_list(words, "και")


            clauses.append({"line_number": lineNum, "words": words, "delimiters": delimiters[i]})
            # NOTE: the clauses have three values
            # clause[0] gives the line num string from the inputted txt file (the two period separated numbers shown at the beginning of a line)
            # clause[1] gives the array to find words in
            # clause[2] gives the punctuation at the end of the clause



    # return clause list
    # jsf = open("testJSON.json", "w", encoding="utf-8")
    # json.dump(clauses, jsf)
    return clauses

# print(parseGreek("texts/001-i_clement.txt"))