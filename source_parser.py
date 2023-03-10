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
import gclause as gc

# Returns true if string contains a number
def contains_number(s):
    pattern = r'\d+'
    match = re.search(pattern, s)
    return bool(match)

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
    line_counter = 1
    first_line_has_num = False
    clauses = []
    for line in raw_lines:
        clause_counter = 1
        line_num, txt = line.split(" ", 1)
        # If the first line doesn't have a number
        # Set first_line_has_num to false and update the line number and line to appropriate values
        if (not contains_number(line_num) and line_counter==1):
            first_line_has_num = False
            # line_num = str(line_counter) + "." + str(clause_counter)
            txt = line
            line_counter += 1
        # If the first line has a number, set first_line_has_num to true
        elif (contains_number(line_num) and line_counter==1):
            first_line_has_num = True
        # If the first line has a number and the current line has a number, exit the if statement
        elif (first_line_has_num and contains_number(line_num)):
            break
        # If the first did not have a number and the current line does not have a number
        # increment the line number 
        elif (not(first_line_has_num) and not contains_number(line_num)):
            # line_num = str(line_counter) + "." + str(clause_counter)
            txt = line
            line_counter += 1
        else:
            raise Exception("Invalid Line Number Input")

        delimiters = []
        for delim in re.finditer("·|\.|\;", txt):
            delimiters.append(txt[delim.start()])
        line_clauses = re.split("·|\.|\;", txt)

        for i in range(len(line_clauses) - 1):
            # If the file did not provide line numbers, this sets line numbers
            if( not(first_line_has_num)):
                line_num = str(line_counter) + "." + str(clause_counter)
                clause_counter+=1
            
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

            res = gc.gclause()
            res.set_identifier(line_num)         # set the prefix of the line
            res.set_words(words)                # list of the Greek words
            res.set_delimiter(delimiters[i])    # punctuation at end of sentence
            res.set_clause(line_num + " " + " ".join(words) + delimiters[i])     # full clause
            clauses.append(res)

    # return clause list
    return clauses