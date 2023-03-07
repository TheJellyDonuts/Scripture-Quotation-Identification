'''
Kai Delsing
03-07-2023

PROBABILISTIC ANALYSIS
TODO <description needed>

NOTE the python library numpy must be installed in order to run average_analysis 
'''


import math
#import numpy as np


outtext = []

with open("prob_analysis_raw.json", "r") as f:
    clause_data = f.readlines()

# performs a simple analysis, which finds the verse with the maximum number of
# matches for a given clause
# returns a list of 
def simple_analysis():
    for clause in clause_data:
        linenum, versemap = clause[0], clause[1]
        versedata = versemap.items()
        versedata.sort(key=lambda x: x[1])
        verse, n = versedata[0]
        outtext += f'Line {linenum} is most likely {verse}, with {n} matches!'
        return outtext
    
def average_analysis():
    for linenum, versemap in clause_data:
        versedata = versemap.items()
        versedata.sort(key=lambda x: x[1])
        av = 0
        for num in versedata[1]:
            av += num
        av = math.ceil(av/len(versedata))
        above_av = []
        for v in versedata:
            if v[1] > av:
                above_av += v
        
        for v in above_av:
            verse, n = v[0]

            outtext += f'Line {linenum} is most likely {verse}, with {n} matches ({n-av} above average)!'
        return outtext