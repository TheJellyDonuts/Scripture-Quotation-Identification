'''
Kai Delsing
03-09-2023

~ ~ GREEK RESULT (gresult) OBJECT CLASS ~ ~
Creates a class gresult (greek result) that has 2 attributes:
- clause: the sentence/clause which this object is centered around
- verses: a dict with keys as verses, and values as a list
         [verse, occurrences]

The verse format is BookCCCVVV. Ex: Matthew010002 (Matthew 10:2)
'''

class gresult():
    def __init__(self):
        self.clause = None
        self.verses = {}

    def set_clause(self, clause):
        self.clause = clause

    def add_verse(self, verse, occurrences):
        self.verses.update({verse: occurrences})
    
    def set_verses(self, verses):
        self.verses = verses