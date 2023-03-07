'''
Stephen Venable
03-06-2023

DIACRITICAL FILTER
This program performs the equivalent function of the Center for New Testament Restoration
    Greek Character Tool (https://greekcntr.org/charutil/index.htm). It takes in a document
    from a given filepathin Greek unicode, removes diacritical marks, lowercases the text, 
    and writes it to a given filepath.

NOTE the python library unicodedata is required to be installed in order to run this program.
'''

import unicodedata

# filter data in input_file, and send the results to output_file
def diacritical_filter(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        greek_text = f.read()

    # remove diacritical marks from greek text and set text to lowercase
    clean_text = ''.join(c for c in unicodedata.normalize('NFD', greek_text) if unicodedata.category(c) != 'Mn')
    clean_text = clean_text.lower()

    # replace final sigmas with regular sigmas
    clean_text = clean_text.replace("ς", "σ")

    # replace semicolons with middle dot
    clean_text = clean_text.replace(";", "·")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(clean_text)
