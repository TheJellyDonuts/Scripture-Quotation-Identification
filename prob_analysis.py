'''
Kai Delsing
03-07-2023

~ ~ PROBABILISTIC ANALYSIS ~ ~
Analyze the data created by the probabalistic data synthesis (prob_data). Multiple
methods of analysis are used:
1. simple_analysis
    - find the verse with the maxmimum number of verse occurences
2. average_analysis
    - find verses with more occurences than the average + standard deviation

NOTE the python library numpy must be installed in order to run average_analysis 
'''


import math
import numpy as np
import json


with open("data/prob_analysis_raw.json", "r") as f:
    clause_data = json.load(f)

# performs a simple analysis, which finds the verse with the maximum number of
# matches for a given clause
# returns a list of results by clause (the outtext+=... line)
def simple_analysis():
    outtext = []
    for clause in clause_data:
        linenum, versemap = clause[0], clause[1]
        versedata = list(versemap.items())
        # sort items by occurence
        versedata.sort(key=lambda x: x[1], reverse = True)

        # grab top item (most occurences)
        verse, n = versedata[0]

        # export
        outtext += f'Line {linenum} is most likely {verse}, with {n} matches!'
        return outtext
    
# performs an average analysis, which finds the average number and standard deviation
# of occurences and only selects verses with an occurence greater than the 
# average + stdev
# returns a list of results by clause (the outtext+=... line)
def average_analysis():
    for clause in clause_data:
        linenum, versemap = clause[0], clause[1]
        versedata = list(versemap.items())
        versedata.sort(key=lambda x: x[1], reverse = True)
        av = 0
        nums = []
        for num in versedata[1]:
            av += num
            nums += num
        av = math.ceil(av/len(versedata))
        above_av = []
        sd = np.std(nums)

        # if given verse's occurences is outside of the stdev of the average,
        # add to list
        for v in versedata:
            if v[1] > (av + sd):
                above += v
        
        # if there are no verses above av+stdev, grab the max and send to outtext
        if len(outtext) == 0:
            verse, n = versedata[0]
            return f'Line {linenum} has no outstanding verse matches. The closest match is {verse}.'
        
        for v in above:
            verse, n = v[0]
            outtext += f'Line {linenum} is most likely {verse}, with {n} matches ({n-av} above average)!'

        return outtext