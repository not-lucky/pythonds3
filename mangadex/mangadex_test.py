import json
from pprint import pprint as pp

with open(r"S:\Everything\mca\lone.json") as fl:
    data = json.load(fl)

pp(data[0])
for lis in data:
    if lis[-1]['group'][0] == 'Flame Scans':
        print(lis[1])