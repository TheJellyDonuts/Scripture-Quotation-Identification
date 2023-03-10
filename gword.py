'''
Kai Delsing
03-06-2023

~ ~ GREEK WORD (gword) OBJECT CLASS ~ ~
Creates a class gword (greek word) that has 2 attributes:
- word: the word which this object is centered around
- verse occurrences: a dict with keys as verses, and values being 
                    a list [verse, count]
When add_verse() is called, if the verse already exists, its 
respective counter is incremented. Otherwise, a new verse pair
is added to the dict.
The verse format is BookCCCVVV. Ex: Matthew010002 (Matthew 10:2)
'''

class gword:
    def __init__(self, word=""):
        self.word = word
        self.verse_occurences = {}

    # set word to given word
    # returns the set word
    def set_word(self, word):
        self.word = word
        return self.word
        
    # insert a verse into verse dict
    # if verse already exists, increment existing verse
    # returns given verse reference
    def add_verse(self, verse):
        if verse in self.verse_occurences.keys():
            v, c = self.verse_occurences[verse]
            c += 1
            self.verse_occurences[verse] = [v, c]
        else:
            self.verse_occurences.update({verse: [verse, 1]})

        return verse
    
    # get [verse,count] pair
    def get_by_verse(self, verse):
        return self.verse_occurences[verse]

    # get count of verse
    def get_count(self, verse):
        return self.verse_occurences[verse][1]

    # check through variants to see if given variant exists
    def is_match(self, matched):
        return matched == self.word