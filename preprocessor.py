'''
Stephen Venable
03-06-2023

NEW TESTAMENT PREPROCESSOR
The goal of the preprocessor is to parse the data contained in words.csv
into a list of gword objects and writes that to wordList.json.

Explanation of functions:
    1. remove_bom - removes binary object model indicator at the beginning of words.csv.
    2. change_verse_id - changes verse id column to BooknameCCCVVVV format from BBBCCCVVV format
'''

import csv
import gword

books = {
    40: 'Matthew',
    41: 'Mark',
    42: 'Luke',
    43: 'John',
    44: 'Acts',
    45: 'Romans',
    46: 'CorinthiansI',
    47: 'CorinthiansII',
    48: 'Galatians',
    49: 'Ephesians',
    50: 'Philippians',
    51: 'Colossians',
    52: 'ThessaloniansI',
    53: 'ThessaloniansII',
    54: 'TimothyI',
    55: 'TimothyII',
    56: 'Titus',
    57: 'Philemon',
    58: 'Hebrews',
    59: 'James',
    60: 'PeterI',
    61: 'PeterII',
    62: 'JohnI',
    63: 'JohnII',
    64: 'JohnIII',
    65: 'Jude',
    66: 'Revelation'
}

# TODO <description needed>
def remove_bom(filename):
    # Read the file as bytes
    with open(filename, 'rb') as f:
        content = f.read()

    # Check for the byte order mark
    bom = b'\xef\xbb\xbf'
    if content.startswith(bom):
        # Remove the byte order mark
        content = content[len(bom):]

        # Write the file back out without the byte order mark
        with open(filename, 'wb') as f:
            f.write(content)

# TODO <description needed>
def change_verse_id(array):
    for row in array:
        book_index = int(str(row[0])[:2])
        new_verse_id = books[book_index]+str(row[0])[2:]
        row[0] = new_verse_id
    return array

# TODO <description needed>

filename = 'words.csv'
# Removes BOM at the beginning of the file
remove_bom(filename)

# Converts CSV File into a 2D Array
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    data_array = [row for row in reader]

# Renames the Verses's ID to use Book Name instead of Book Number
change_verse_id(data_array)

greek_words = []
for value in data_array:
    in_array = False
    verse_ref = value[headers.index("VerseID")]
    array_word = value[headers.index("Word")]
    for greek_word in greek_words:
        # Checks to see if word is already in array
        if(array_word == greek_word.word):
            # If word is in array, add verse to current word
            greek_word.add_verse(verse_ref)
            in_array = True
            break
    if not in_array:
        # Sets Word Value
        new_word = gword.gword(word=array_word)
        new_word.add_verse(verse_ref)
        greek_words.append(new_word)

# Print Greek Word Array as a JSON File
with open('data/word_list.json', 'w') as f:
    f.writelines("[")
    lst = [word.export_json()+",\n" for word in greek_words]
    lst[-1] = lst[-1][:-2]+"\n"
    f.writelines(lst)
    f.writelines("]")