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
cereals = []

def parse():
    with open("static/data/cereal.csv", "r") as f:
        for line in f:
            info = line.split(" ")
            info[0] = info[0].replace("_"," ")
            info[1] = symbol_table[info[1]]
            end = info[len(info)-1]
            info[len(info)-1] = end[0:len(end)-1]
            cereal = {
                "name": info[0],
                "manufacturer": info[1],
                "temperature": info[2],
                "calories": info[3],
                "protein": info[4],
                "fat":info[5],
                "sodium": info[6],
                "fiber": info[7],
                "carbs": info[8],
                "sugars": info[9],
                "shelf": info[10],
                "potassium": info[11],
                "vitamins": info[12],
                "weight": info[13],
                "serving": info[14]
             }
            cereals.append(cereal)
    return json.dumps(cereals)
