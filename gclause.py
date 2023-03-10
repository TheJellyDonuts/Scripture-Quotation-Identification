'''
Kai Delsing
03-09-2023

~ ~ GREEK CLAUSE (gclause) OBJECT CLASS ~ ~
Creates a class gclause (greek clause) that has 3 attributes:
- clause: the sentence/clause which this object is centered around
- identifier: the prefix identifier that makes this line
               distinct (i.e. 1.1)
- words: a list of Greek word strings (not gwords)

The verse format is BookCCCVVV. Ex: Matthew010002 (Matthew 10:2)
'''

class gclause():
    def __init__(self):
        self.clause = ""
        self.identifier = ""
        self.words = []
        self.delimiter = ""

    def set_clause(self, clause):
        self.clause = clause

    def set_identifier(self, id):
        self.identifier = id

    def add_word(self, word):
        self.words += word

    def set_words(self, word):
        self.words = word

    def set_delimiter(self, delim):
        self.delimiter = delim