# parses the csv file
import json
global symbol_table, cereals
symbol_table = { "A": "American Home Food Products",
                 "G": "General Mills",
                 "K": "Kellogs",
                 "N": "Nabisco",
                 "P": "Post",
                 "Q": "Quaker Oats",
                 "R": "Ralston Purina",
                 "H": "Hot",
                 "C": "Cold" }
cereals = {}

def parse():
    with open("cereal.csv", "r") as f:
        for line in f:
            info = line.split(" ")
            info[0] = info[0].replace("_"," ")
            info[1] = symbol_table[info[1]]
            end = info[len(info)-1]
            info[len(info)-1] = end[0:len(end)-1]
            cereals[info[0]] = info[1:]
    return json.dumps(cereals)
