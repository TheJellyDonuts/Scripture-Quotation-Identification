import greekParser
import json

clauses, words = []
clauses = greekParser.parseGreek("texts/001-i_clement.txt")
#with open('clauseList.json', 'r', encoding='UTF-8') as f:
#    clauses = f.readlines()


with open('wordList.json', 'r') as f:
    words = f.readlines()

cache = {} # word: [[verse, occurences],[verse, occurences],...]
# TODO: clear cache at some point? 

versemap = {} # verse: occurences
not_found = {}
output = []

def inc_versemap(verselist):
    # [verse, occurences]
    # increment occurences
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
def add_to_cache(pair):
    word, verselist = pair
    cache.update({word: verselist})

for clause in clauses:
    # go through a clause for each word
    for word in clause["words"]:
        found = False

        # search cache for the word; if found, increment
        if check_cache(word):
            found = True
            inc_versemap(cache[word])

        # search wordlist & variants for the word
        else:
            for word_obj in words:
                if word_obj.is_variant(word):
                    found = True
                    inc_versemap(word_obj.verse_occurences)
                    add_to_cache(word_obj)

        # if word not found in cache or wordlist, add to not_found
        # list. Keep track of occurences
        if not found:
            if word not in not_found:
                not_found.update({word: 1})
            else:
                not_found[word] += 1

    # TODO: deal with punctuation
    
    # add data to output and clear cache
    output += [clause["line_number"], versemap]
    cache.clear()


# output

with open("prob_analysis_raw.txt", "wr"):
    output.writelines()
    "\n\nWords not found:".writeline()
    not_found.writelines()

# TODO: actually do an analysis
