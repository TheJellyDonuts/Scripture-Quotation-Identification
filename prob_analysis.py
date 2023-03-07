



outtext = []

with open("prob_analysis_raw.txt", "a") as f:
    clause_data = f.readlines()


for linenum, versemap in clause_data:
    
    outtext += f'Line {linenum} is most likely {verse}, with {n} matches!'