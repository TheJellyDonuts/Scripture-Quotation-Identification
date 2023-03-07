'''
Michael White
03-07-2023

Data visualization tools
TODO <description needed>
'''

# plotting imports
import numpy as np
import matplotlib.pyplot as plt
import json

with open("data/prob_analysis_raw.json", "r") as f:
    clause_data = json.load(f)

ntDict = {
    "Matthew": (40, "Matt"),
    "Mark": (41, "Mark"),
    "Luke": (42, "Luke"),
    "John": (43, "John"),
    "Acts": (44, "Acts"),
    "Romans": (45, "Rom"),
    "CorinthiansI": (46, "1 Cor"),
    "CorinthiansII": (47, "2 Cor"),
    "Galatians": (48, "Gal"),
    "Ephesians": (49, "Eph"),
    "Philippians": (50, "Philip"),
    "Colossians": (51, "Col"),
    "ThessaloniansI": (52, "1 Thes"),
    "ThessaloniansII": (53, "2 Thes"),
    "TimothyI": (54, "1 Tim"),
    "TimothyII": (55, "2 Tim"),
    "Titus": (56, "Titus"),
    "Philemon": (57, "Philem"),
    "Hebrews": (58, "Heb"),
    "James": (59, "James"),
    "PeterI": (60, "1 Pet"),
    "PeterII": (61, "2 Pet"),
    "JohnI": (62, "1 Jo"),
    "JohnII": (63, "2 Jo"),
    "JohnIII": (64, "3 Jo"),
    "Jude": (65, "Jude"),
    "Revelation": (66, "Rev")
}

# array of linenum, verse, matchval

# get data for analysis

# bar graph of one verse
def genGraph(lineNum, verseData, numBars = 50, matchThreshold = 0):

    # initialize arrays
    x = np.array([])
    y = np.array([])
    barcount = 0

    # get data
    for verse, n in verseData:
        # check for extra params
        if barcount >= numBars or n < matchThreshold:
            break            

        # add bar data
        bk, chp, vrs = formatVerse(verse)
        x = np.append(x, ntDict[bk][1] + " " + str(chp) + ": " + str(vrs))
        y = np.append(y, n)

        barcount += 1

    if barcount > 0:

        # set up new figure
        plt.figure()

        # generate graph
        plt.bar(x, y)
        plt.title("verse matches for line " + lineNum)
        plt.xlabel("verse")
        plt.xticks(rotation = -90)
        plt.ylabel("number of word matches")
        plt.tight_layout(pad = 1.5)
        plt.show()

# generates bar graphs for all verses
def genBars(maxNum = 99999999, numBars = 10, minThresh = 3):
    graphCount = 0
    for clause in clause_data:
        linenum, versemap = clause[0], clause[1]
        if graphCount >= maxNum:
            break
        versedata = list(versemap.items())
        versedata.sort(key=lambda x: x[1], reverse = True)
        genGraph(linenum, versedata, numBars, minThresh)

        graphCount += 1
        
        

# extracts useful information from verse string
def formatVerse(vrsStr):
    book = vrsStr[:-6]
    chapNum = int(vrsStr[-6:-3])
    verseNum = int(vrsStr[-3:])
    return book, chapNum, verseNum

# print(ntDict[formatVerse("Matthew028019")[0]][1])
genBars(20, 10, 3)

