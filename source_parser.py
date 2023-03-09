'''
Michael White
03-06-2023

SOURCE GREEK PARSER
Takes an input file and produces a list of clauses found in the file

The file must be formatted with the diacritical filter found in diacritical.py
The file must also be in koine greek and each line must start with an identifying line number followed by a spce character
(e.g. "12.4  <Greek text>")

The parser removes all the definite articles 
It also splits the lines into clauses which are determined by being separated by the greek equivalents of the characters '.', ':' and '?'
The re library provides regex functionality for splitting the lines

The output is described right above the return statement
'''


import re
import diacritical

# remove all items from a list with a given value 
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


def parse_greek(input_file):
    # import file from given filepath
    out_file = "data/filtered.txt"
    diacritical.diacritical_filter(input_file, out_file)
    with open(out_file, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    # find lines
    clauses = []
    for line in raw_lines:
        line_num, txt = line.split(" ", 1)
        delimiters = []
        for delim in re.finditer("·|\.|\;", txt):
            delimiters.append(txt[delim.start()])
        line_clauses = re.split("·|\.|\;", txt)

        for i in range(len(line_clauses) - 1):
            
            # find words
            words = line_clauses[i].split(" ")

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


            clauses.append({"line_number": line_num, "words": words, "delimiters": delimiters[i]})
            # NOTE: the clauses have three values
            # clause[0] gives the line num string from the inputted txt file (the two period separated numbers shown at the beginning of a line)
            # clause[1] gives the array to find words in
            # clause[2] gives the punctuation at the end of the clause

    # return clause list
    return clauses