'''
Kai Delsing
03-09-2023

~ ~ GREEK RESULT (gresult) OBJECT CLASS ~ ~
Creates a class gresult (greek result) that has 2 attributes:
- clause: the prefix identifier that makes this line
          distinct (i.e. 1.1)
- verses: a dict with keys as verses, and values as a list
         [verse, occurrences]

The verse format is BookCCCVVV. Ex: Matthew010002 (Matthew 10:2)
'''

class gresult():
    def __init__(self):
        self.identifier = None
        self.verses = {}

    def set_id(self, clause):
        self.clause = clause

    def add_verse(self, verse, occurrences):
        self.verses.update({verse: occurrences})
    
    def set_verses(self, verses):
        self.verses = verses