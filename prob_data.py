'''
Kai Delsing
03-06-2023

~ ~ PROBABILISTIC DATA SYNTHESIS ~ ~

This file takes in two primary data files and synthesizes them together
    1. Word List (JSON) - a collection of all of the NT gword objects
    2. Clause List (JSON) - a collection of each of the clauses from the input text

After taking the files in, this program distributes the data into these lists and dictionaries:
1. versemap
    - a dictionary with keys as unique verses, and values of the number of occurences
        in a given clause
    - structure: {verse: occurences, verse:occurences, ...}
2. not_found
    - a dictionary containing each of the words that were not found in the wordlist, and 
        how many times they occurred
    - structure: {verse: occurences, verse:occurences, ...}
3. cache
    - a dictionary cleared with each new clause that stores new occurences of words
        in a clause, to try and lower the computational cost of being forced to search
        the entire wordlist each time
    - structure: {word: [verse, occurences],[verse, occurences],...], 
                  word: [verse, occurences],[verse, occurences],...], ...}

The program will iterate by clause. It goes through each clause, searching each word first in 
    the cache, then in the wordlist if it is not found in the cache. If the word is found,
    the versemap and cache are updated accordingly; if it is not, not_found is updated.

At the completion of each clause, the versemap results are pushed to an output list, along
    with the line number. The not_found dict is *not* cleared after each clause, unlike the
    cache and versemap.
'''

import source_parser
import json
import gword

clauses, words = [], []
clauses = source_parser.parseGreek("texts/001-i_clement.txt")
#with open('clauseList.json', 'r', encoding='UTF-8') as f:
#    clauses = f.readlines()


with open('wordList.json', 'r') as f:
    # words = f.readlines()
    data = json.load(f)

# Place Word Data in list of Objects
words = []
for word in data:
    new_word_obj = gword.gword()
    new_word_obj.import_json(word)
    words.append(new_word_obj)


cache = {} # word: [verse, occurences],[verse, occurences],...]

versemap = {} # verse: occurences
not_found = {}
output = []

# increment the versemap for each verse in verselist
def inc_versemap(verselist):
    # [verse, occurences]
    # TODO: this doesn't deal with the fact that some words are more common in certain verses
    for verse, occurences in verselist:
        if verse in versemap:
            versemap[verse] += 1
        else:
            versemap.update({verse: 1})

# return if the given word is found in cache 
def check_cache(word):
    # check if given word is in cache
    if word in cache.keys():
        return True
    return False

# add a new word-verselist pair to the cache
def add_to_cache(word, verselist):
    cache.update({word: verselist})

def search_wordlist(word):
    for word_obj in words:
        if word_obj.is_match(word):
            inc_versemap(word_obj.verse_occurences.values())
            add_to_cache(word_obj.word, word_obj.verse_occurences.values())
            return True
    return False

# go through a clause for each word
for clause in clauses:
    for word in clause["words"]:
        found = False

        # search cache for the word; if found, increment respective
        # verses in versemap
        if check_cache(word):
            found = True
            inc_versemap(cache[word])

        # search wordlist & variants for the word
        else:
            # iterate through wordlist and add if found
            found = search_wordlist(word)

        # if word not found in cache or wordlist, add to not_found
        # list. Keep track of occurences
        if not found:
            if word not in not_found:
                not_found.update({word: 1})
            else:
                not_found[word] += 1

    # TODO: deal with punctuation

    # add data to output and clear cache
    # output += [clause["line_number"], versemap]
    output.append([clause["line_number"], versemap.copy()])
    cache.clear()
    versemap.clear()


# output

with open("prob_analysis_raw.json", "w") as f:
    json.dump(output, f)

with open("not_found_words.txt", 'w', errors='ignore') as f:
    f.writelines("Words not found:")
    f.writelines(not_found)