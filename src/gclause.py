'''
Kai Delsing
03-09-2023

~ ~ GREEK CLAUSE (gclause) OBJECT CLASS ~ ~
Creates a class gclause (greek clause) that has 4 attributes:
1. clause: The actual string clause itself, with prefix and trailing punctuation
2. identifier: the prefix or line number that precedes the clause itself
3. words: a list of Greek word (not gword) strings that the clause contains
4. delimiter: the postfix punctuation of the clause

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

    def __str__(self):
        s = ''
        s += 'Clause: ' + self.clause + '; '
        s += 'Identifier: ' + self.identifier  + '; '
        s += 'Words: ' + ', '.join(self.words)  + '; '
        s += 'Delimiter: ' + self.delimiter
        return s