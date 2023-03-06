# Kai Delsing
# 3-6-2023
'''
Creates a class gword (greek word) that has 3 attributes:
- word # the word which this object is centered around
- variants # other acceptable forms of the central word
- verse occurences # a dict with keys as verses, and values being 
                    a list [verse, count]
When add_verse() is called, if the verse already exists, its 
respective counter is incremented. Otherwise, a new verse pair
is added to the dict.
The verse format is BookCCCVVV. Ex: Matthew010002 (Matthew 10:2)
'''

import json

class gword:
    def __init__(self, word="", variants=[], verse_occurences={}):
        self.word = word
        self.variants = variants
        self.verse_occurences = verse_occurences

    # set word to given word
    # returns the set word
        def set_word(self, word):
            self.word = word
            return self.word
        

    # append a variant to the variant list
    # returns given variant
    def add_variant(self, variant):
        self.variants.append(variant)
        return variant

    # insert a verse into verse dict
    # if verse already exists, increment existing verse
    # returns given verse reference
    def add_verse(self, verse):
        if verse in self.verse_occurences.keys():
            self.verse_occurences[verse][1] += 1
        else:
            self.verse_occurences.update({verse: 1})

        return verse
    
    # get [verse,count] pair
    def get_by_verse(self, verse):
        return self.verse_occurences[verse]

    # get count of verse
    def get_count(self, verse):
        return self.verse_occurences[verse][1]

    # check through variants to see if given variant exists
    def is_variant(self, variant):
        return variant in self.variants
    
    # import a JSON object and update this gword object
    def import_json(self, import_dict):
        try:
            self.word = import_dict["word"]
            self.variants = import_dict["variants"]
            self.verse_occurences = import_dict["verse_occurences"]
        except:
            print("Error encountered importing word object")

    # export this gword object to a JSON object
    def export_json(self):
        export_dict = {
            "word": self.word,
            "variants": self.variants,
            "verse_occurences": self.verse_occurences
        }
        json_obj = json.dumps(export_dict, indent=4)
        return json_obj