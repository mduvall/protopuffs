# parses the csv file
import json
global symbol_table, cereals, count
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
carb_fat_cereals = []
fiber_cereals = {}
salt_cereals = []
def parse():
    count = 0
    with open("static/data/cereal.csv", "r") as f:
        for line in f:
            info = line.split(" ")
            info[0] = info[0].replace("_"," ")
            info[1] = symbol_table[info[1]]
            end = info[len(info)-1]
            info[len(info)-1] = end[0:len(end)-1]
            count+=1
            if not (float(info[8]) == -1) and not (float(info[4]) == -1) and not (float(info[5]) == -1):
                carb_fat_cereals.append({
                        "calories":float(info[3]),
                        "protein":float(info[4]),
                        "fat":float(info[5]),
                        "name":info[0],
                        "carbs":float(info[8])})
            if not (float(info[7]) == -1):
                try:
                    fiber_cereals[info[1]] = [fiber_cereals[info[1]][0]+float(info[7]),fiber_cereals[info[1]][1]+1]
                except KeyError:
                    fiber_cereals[info[1]] = [float(info[7]),1]
            print info[0], info[6], info[12]
            if not (float(info[12]) == -1) and not (float(info[6]) == -1):
                salt_cereals.append({
                    "name":info[0],
                    "sodium":float(info[6]),
                    "vitamins":float(info[12])})
    meaned_fiber_cereals = []
    for manu in fiber_cereals:
        meaned_fiber_cereals.append({
                "name":manu,
                "fiber":(fiber_cereals[manu][0]/fiber_cereals[manu][1])})
    print json.dumps(salt_cereals, indent=4)
    return [json.dumps(carb_fat_cereals), json.dumps(meaned_fiber_cereals), json.dumps(salt_cereals)]
