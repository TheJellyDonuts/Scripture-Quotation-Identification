import csv
import gword
import itertools

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

def read_csv_to_dict(filename):
    """
    Reads a CSV file and returns a dictionary with headers as keys and
    data as values.
    """
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        data = {row['VerseID']: {'CollationID': row['CollationID'], 
                                 'VariantID': row['VariantID'], 
                                 'Word': row['Word'], 
                                 'ASCII': row['ASCII'], 
                                 'Accented': row['Accented']} 
                for row in reader}
        return data


def change_verse_id(dictname):
    new_dict = {}
    for row in dictname:
        book_index = int(str(row)[:2])
        new_key = books[book_index]+str(row)[2:]
        new_dict[new_key] = dictname[row]
    return new_dict

filename = 'words.csv'
# Removes BOM at the beginning of the file
remove_bom(filename)

# Converts CSV file into a Dictionary
data_dict = read_csv_to_dict(filename)

# Renames the Dictionary's Keys to use Book Name instead of Book Number
greek_dict = change_verse_id(data_dict)

# for row in greek_dict[1:100]:
#     print(greek_dict[row]['CollationID'] + " " + greek_dict[row]['Word'] + " " + greek_dict[row]['Accented'])

greek_words = []
for key, value in itertools.islice(greek_dict.items(), 10):
    in_array = False
    for greek_word in greek_words:
        # Checks to see if word is already in array
        if(value['Word'] == greek_word.word):
            # If word is in array, add verse to current word
            greek_word.add_verse(key)
            in_array = True
            break
    if not in_array:
        # Sets Word Value
        new_word = None
        new_word = gword.gword(word=value['Word'])
        print(new_word)
        new_word.add_verse(key)
        greek_words.append(new_word)

for greek_word in greek_words:
    print("Word: " + greek_word.word + " Count: " + str(greek_word.verse_occurences))