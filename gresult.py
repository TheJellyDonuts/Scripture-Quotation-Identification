'''
Kai Delsing
03-09-2023

~ ~ GREEK RESULT (gresult) OBJECT CLASS ~ ~
Creates a class gresult (greek result) that has 2 attributes:
- clause: the actual string clause itself, with prefix and 
          trailing punctuation
- identifier: the prefix identifier that makes this line
          distinct (i.e. 1.1)
- verses: a dict with keys as verses, and values as a list
         [verse, occurrences]

The verse format is BookCCCVVV. Ex: Matthew010002 (Matthew 10:2)
'''

class gresult():
    def __init__(self):
        self.clause = ""
        self.identifier = None
        self.verses = {}

    def set_clause(self, clause):
        self.clause = clause

    def set_id(self, id):
        self.identifier = id

    def add_verse(self, verse, occurrences):
        self.verses.update({verse: occurrences})
    
    def set_verses(self, verses):
        self.verses = verses

    def __str__(self):
        s = f"Clause: {self.clause}\n"
        s += f"\tIdentifier: {self.identifier}\n"
        s += f"\tVerses: {self.verses}\n"
        return s