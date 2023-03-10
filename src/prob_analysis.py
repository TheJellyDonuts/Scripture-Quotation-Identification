'''
Kai Delsing
03-07-2023

~ ~ PROBABILISTIC ANALYSIS ~ ~
Analyze the data created by the probabilistic data synthesis (prob_data). Multiple
methods of analysis are used:
1. simple_analysis
    - find the verse with the maximum number of verse occurrences
2. average_analysis
    - find verses with more occurrences than the average + standard deviation

NOTE the python library numpy must be installed in order to run average_analysis 
'''


import math
import numpy as np
import pickle

# Function opens prob_analysis_raw.pkl and returns the load
def load_prob_raw():
    with open("data/prob_analysis_raw.pkl", "rb") as inp:
        return pickle.load(inp)

# performs a simple analysis, which finds the verse with the maximum number of
# matches for a given clause
# returns a list of results by clause (the outtext+=... line)
def simple_analysis(include_clause=False):
    clause_res = load_prob_raw()
    with open("data/prob_analysis_raw.pkl", "rb") as inp:
        clause_res = pickle.load(inp)
    outtext = []
    for clause in clause_res:
        linenum, versemap = clause.identifier, clause.verses
        versedata = list(versemap.items())
        # sort items by occurence
        versedata.sort(key=lambda x: x[1], reverse = True)
        # grab top item (most occurences)
        if len(versedata) == 0:
            continue
        verse, n = versedata[0]

        # export
        if include_clause:
            outtext += [clause.clause]
            outtext += [f'\n\t{verse} has {n} word matches!']
        else:
            outtext += [f'Line {linenum} is most likely {verse}, with {n} word matches!']
        outtext += ['\n']
    return outtext
    
# performs an average analysis, which finds the average number and standard deviation
# of occurences and only selects verses with an occurence greater than the 
# average + (stdev*num_sd)
# returns a list of results by clause (the outtext+=... line)
def average_analysis(include_clause=False, num_sd=3):
    outtext = []
    clause_res = load_prob_raw()
    for clause in clause_res:
        linenum, versemap = clause.identifier, clause.verses
        versedata = list(versemap.items())
        versedata.sort(key=lambda x: x[1], reverse = True)
        occurrences = [x[1] for x in versedata]

        # if no words in common with any verse
        if len(versedata) == 0:
            continue

        # calculate the average and standard deviation
        av = math.ceil(np.average(occurrences))
        sd = math.ceil(np.std(occurrences))
        above = []

        # if given verse's occurences is outside of the stdev of the average,
        # add to list
        for v in versedata:
            if v[1] > av + sd*num_sd:
                above += [v]
        
        # if the include_clause printing option is enabled
        if include_clause:
            outtext += "\n" + clause.clause

            # if there are no verses above av+stdev, grab the max and send to outtext
            if len(above) == 0:
                verse, n = versedata[0]
                outtext += [f'\n\tNo outstanding verse matches found; closest match is {verse}.']
            
            for v in above:
                verse, n = v
                outtext += [f'\n\t{verse} has {n} word matches ({n-av} above average)!']
 
        # if the include_clause printing option is disabled
        else:
            # if there are no verses above av+stdev, grab the max and send to outtext
            if len(above) == 0:
                verse, n = versedata[0]
                outtext += [f'Line {linenum} has no outstanding verse matches; closest match is {verse}.']
            
            for v in above:
                verse, n = v
                outtext += [f'Line {linenum} is most likely {verse}, with {n} word matches ({n-av} above average)!']

        outtext += '\n'
    return outtext