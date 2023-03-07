import unicodedata

# Path to Input File
input_file = ""
# Path to Output File
output_file = ""

with open(input_file, "r", encoding="utf-8") as f:
    greek_text = f.read()

# remove diacritical marks from greek text and set text to lowercase
clean_text = ''.join(c for c in unicodedata.normalize('NFD', greek_text) if unicodedata.category(c) != 'Mn')
clean_text = clean_text.lower()

# replace final sigmas with regular sigmas
clean_text = clean_text.replace("ς", "σ")

# replace semicolons with middle dot
clean_text = clean_text.replace(";", "·")

# # replace periods with middle period
# clean_text = clean_text.replace(".", "·")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(clean_text)
