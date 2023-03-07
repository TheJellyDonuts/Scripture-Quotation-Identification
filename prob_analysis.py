



outtext = []

with open("prob_analysis_raw.txt", "a") as f:
    clause_data = f.readlines()

def simple_analysis():
    for linenum, versemap in clause_data:
        versedata = versemap.items()
        versedata.sort(key=lambda x: x[1])
        verse, n = versedata[0]
        outtext += f'Line {linenum} is most likely {verse}, with {n} matches!'