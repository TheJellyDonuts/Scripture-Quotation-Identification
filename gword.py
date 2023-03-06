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

class gword:
    def __init__(self, word="", variants=[], verse_occurences={}):
        self.word = word
        self.variants = variants
        self.verse_occurences = verse_occurences

    # append a variant to the variant list
    def add_variant(self, variant):
        self.variants.append(variant)
        return variant

    # insert a verse into verse dict
    # if verse already exists, increment existing verse
    def add_verse(self, verse):
        if verse in self.verse_occurences.keys():
            self.verse_occurences[verse][1] += 1
        else:
            self.verse_occurences.update({verse: 1})
    
    # get verse,count pair
    def get_by_verse(self, verse):
        return self.verse_occurences[verse]

    # get count of verse
    def get_count(self, verse):
        return self.verse_occurences[verse][1]

    # check through variants to see if given variant exists
    def is_variant(self, variant):
        return variant in self.variants