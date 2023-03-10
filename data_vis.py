'''
Michael White
03-07-2023

Data visualization tools
This file contains functions needed to graph data retrieved using prob_analysis.py
gen_graph makes a bar graph of the most similar verses to a given clause
gen_bars calls gen_graph on every clause
gen_stacked_bar provides more comprehensive analysis on which verses are most referenced in the data
'''

# plotting imports
import numpy as np
import matplotlib.pyplot as plt
import pickle

# open file to use
with open("data/prob_analysis_raw.pkl", "rb") as f:
    clause_data = pickle.load(f)

# dictionary for book index and abbreviation
nt_dict = {
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

# generates stacked bar graph to determine which verses are most referenced or matched
# num_bars represents the number of verses' data to display (if 10, the top 10 matched verses will display)
# match_threshold discriminates the number of word matches required between a clause and a verse to be included in the plot
# if bible_ordered is true, the verses will display in order based on the Bible; 
# Otherwise, they will be organized from most to least matches
def gen_stacked_bar(num_bars = 50, match_threshold = 5, bible_ordered = True):

    # create values for computation
    used_lens = list()
    for i in range(75):
        used_lens.append(False)
    max_match = match_threshold
    min_match = 75

    # format data from file
    occur_dict = {}
    for clause in clause_data:
        versemap = clause.verses
        verse_data = list(versemap.items())
        verse_data.sort(key=lambda x: x[1], reverse = True)
        

        # Find the number of clauses that match the verse
        for verse, n in verse_data:
            if n >= match_threshold:
                if n > max_match:
                    max_match = n
                if n < min_match:
                    min_match = n
                used_lens[n] = True

                # update running total of verse usage to include previously unused verse
                if not verse in occur_dict:
                    bk, chp, vrs = format_verse(verse)
                    occur_dict[verse] = {
                        "bookNum": nt_dict[bk][0],
                        "chp": chp,
                        "vrs": vrs,
                        "potentialReferences": {}, 
                        "totalReferences": 0,
                        "bookAbbrev": nt_dict[bk][1]
                    }
                
                # update tallies of verse usage
                temp = occur_dict[verse]
                temp["totalReferences"] += 1
                if not n in temp["potentialReferences"]:
                    temp["potentialReferences"][n] = 1
                else:
                    temp["potentialReferences"][n] += 1
                occur_dict[verse] = temp

    # organize data to fit in stacked bar graph
    verse_usage = [val[1] for val in list(occur_dict.items())]
    verse_usage.sort(key=lambda vrs_obj: vrs_obj["totalReferences"], reverse = True) 
    if len(verse_usage) > num_bars:
        verse_usage = verse_usage[:num_bars]
    if bible_ordered:
        verse_usage.sort(key=lambda vrs_obj: vrs_obj["bookNum"] * 1000000 + vrs_obj["chp"] * 1000 + vrs_obj["vrs"])
    
    # organize bar layers
    bars = list()
    matches = list()
    for i in range(min_match, max_match):
        if used_lens[i]:
            bar_arr = list()
            for vrs_obj in verse_usage:
                if not i in vrs_obj["potentialReferences"]:
                    bar_arr.append(0)
                else:
                    bar_arr.append(vrs_obj["potentialReferences"][i])

            bars.append(np.array(bar_arr))
            matches.append(i)

    # set up new figure
    plt.figure()

    # generate stacked bar graph
    x = list()
    for vrs_obj in verse_usage:
        x.append(vrs_obj["bookAbbrev"] + " " + str(vrs_obj["chp"]) + ": " + str(vrs_obj["vrs"]))

    # set up stacked bars
    curr_bottom = np.zeros(num_bars)
    for bar in bars:
        plt.bar(x, bar, bottom = curr_bottom)
        curr_bottom += bar
    
    # graph visualization
    plt.title("Verses with the most references")
    plt.xlabel("verse")
    plt.xticks(rotation = -90)
    plt.ylabel("number of potential references")
    plt.legend(matches)
    plt.tight_layout(pad = 1.5)
    plt.show()

# bar graph of one clause
def gen_graph(line_num, verse_data, num_bars = 50, match_threshold = 0):

    # initialize arrays
    x = np.array([])
    y = np.array([])
    bar_count = 0

    # get data
    for verse, n in verse_data:
        # check for extra params
        if bar_count >= num_bars or n < match_threshold:
            break            

        # add bar data
        bk, chp, vrs = format_verse(verse)
        x = np.append(x, nt_dict[bk][1] + " " + str(chp) + ": " + str(vrs))
        y = np.append(y, n)

        bar_count += 1

    if bar_count > 0:

        # set up new figure
        plt.figure()

        # generate graph
        plt.bar(x, y)
        plt.title("verse matches for line " + line_num)
        plt.xlabel("verse")
        plt.xticks(rotation = -90)
        plt.ylabel("number of word matches")
        plt.tight_layout(pad = 1.5)
        plt.show()

# generates bar graphs for all verses
def gen_bars(max_num = 99999999, num_bars = 10, min_Thresh = 3):
    graph_count = 0
    for clause in clause_data:
        line_num, versemap = clause.identifier, clause.verses
        if graph_count >= max_num:
            break
        verse_data = list(versemap.items())
        verse_data.sort(key=lambda x: x[1], reverse = True)
        gen_graph(line_num, verse_data, num_bars, min_Thresh)

        graph_count += 1

# extracts useful information from verse string
def format_verse(vrs_str):
    book = vrs_str[:-6]
    chap_num = int(vrs_str[-6:-3])
    verse_num = int(vrs_str[-3:])
    return book, chap_num, verse_num

# print(nt_dict[format_verse("Matthew028019")[0]][1])
gen_stacked_bar(20, 5, True)
gen_bars(50, 10, 7)

