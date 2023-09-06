# TO DO:
# - currently we are storing the ammount of entites per individual map, but not showing it in the final result
# - if possible, rewrite it so we only add the total ammount of entites for readability

import re
import csv

MAP_DIR = "C:\Program Files (x86)\Steam\steamapps\common\Half-Life\\valve\maps"
#exclude t0a0b.bsp, it was split into two map  but kept in the files for some reason
MAP_LIST = ('c0a0.bsp', 'c0a0a.bsp', 'c0a0b.bsp', 'c0a0c.bsp', 'c0a0d.bsp', 'c0a0e.bsp', 'c1a0.bsp', 'c1a0a.bsp', 'c1a0b.bsp', 'c1a0c.bsp', 'c1a0d.bsp', 'c1a0e.bsp', 'c1a1.bsp', 'c1a1a.bsp', 'c1a1b.bsp', 'c1a1c.bsp', 'c1a1d.bsp', 'c1a1f.bsp', 'c1a2.bsp', 'c1a2a.bsp', 'c1a2b.bsp', 'c1a2c.bsp', 'c1a2d.bsp', 'c1a3.bsp', 'c1a3a.bsp', 'c1a3b.bsp', 'c1a3c.bsp', 'c1a3d.bsp', 'c1a4.bsp', 'c1a4b.bsp', 'c1a4d.bsp', 'c1a4e.bsp', 'c1a4f.bsp', 'c1a4g.bsp', 'c1a4i.bsp', 'c1a4j.bsp', 'c1a4k.bsp', 'c2a1.bsp', 'c2a1a.bsp', 'c2a1b.bsp', 'c2a2.bsp', 'c2a2a.bsp', 'c2a2b1.bsp', 'c2a2b2.bsp', 'c2a2c.bsp', 'c2a2d.bsp', 'c2a2e.bsp', 'c2a2f.bsp',
            'c2a2g.bsp', 'c2a2h.bsp', 'c2a3.bsp', 'c2a3a.bsp', 'c2a3b.bsp', 'c2a3c.bsp', 'c2a3d.bsp', 'c2a3e.bsp', 'c2a4.bsp', 'c2a4a.bsp', 'c2a4b.bsp', 'c2a4c.bsp', 'c2a4d.bsp', 'c2a4e.bsp', 'c2a4f.bsp', 'c2a4g.bsp', 'c2a5.bsp', 'c2a5a.bsp', 'c2a5b.bsp', 'c2a5c.bsp', 'c2a5d.bsp', 'c2a5e.bsp', 'c2a5f.bsp', 'c2a5g.bsp', 'c2a5w.bsp', 'c2a5x.bsp', 'c3a1.bsp', 'c3a1a.bsp', 'c3a1b.bsp', 'c3a2.bsp', 'c3a2a.bsp', 'c3a2b.bsp', 'c3a2c.bsp', 'c3a2d.bsp', 'c3a2e.bsp', 'c3a2f.bsp', 'c4a1.bsp', 'c4a1a.bsp', 'c4a1b.bsp', 'c4a1c.bsp', 'c4a1d.bsp', 'c4a1e.bsp', 'c4a1f.bsp', 'c4a2.bsp', 'c4a2a.bsp', 'c4a2b.bsp', 'c4a3.bsp', 'c5a1.bsp',
            't0a0.bsp', 't0a0a.bsp', 't0a0b1.bsp', 't0a0b2.bsp', 't0a0c.bsp', 't0a0d.bsp')
ENTITY_PATTERN = "\"classname\" \"\w*\""

data = {}

def add_to_data(match_list):
    for entity in match_list:
        if entity not in data:
            data[entity] = 1
        else:
            data[entity] += 1


def make_readable_list(findings):
    results = []
    # remove the '"classname" ' part and the quotations
    for x in findings:
        x = str(x).replace("\"", "")
        x = x.replace("classname ", "")
        results.append(x)
    return results

# # for individual map data
# def make_entity_dictionary(match_list):
#     match_dict = {}
#     for x in match_list:
#         if x not in match_dict:
#             match_dict[x] = 1
#         else:
#             match_dict[x] += 1
#     return match_dict

#the data is stored in a dicionary,  where each key is the entity and the value is the amount
def make_csv_file(data):
    with open("entity_results.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["entity", "amount"])
        for key, value in data.items():
            writer.writerow([key, value])


def search_file(file_path, pattern):
    with open(file_path, "rb") as file:
        data = file.read()

    # Decode the readable parts of the file into a string
    text = ''
    for byte in data:
        if 32 <= byte <= 126:
            # This is a printable ASCII character, so add it to the string
            text += chr(byte)
        else:
            # This is not a printable ASCII character, so add a space instead
            text += ' '

    # Count the number of occurrences of the search string in the text
    findings = re.findall(pattern, text)
    return make_readable_list(findings)


map_dict = {}
#entity_total = 0

for maps in range(len(MAP_LIST)):
    current_map_path = f"{MAP_DIR}\\{MAP_LIST[maps]}"
    current_map_name = MAP_LIST[maps]

    matches_list = search_file(current_map_path, ENTITY_PATTERN)

    add_to_data(matches_list)

    # #for individual map data
    #matches_dict = make_entity_dictionary(matches_list)


    # #these are the results for each individual map
    #map_dict[current_map_name] = {}
    #map_dict[current_map_name]["entity_dict"] = matches_dict
    #map_dict[current_map_name]["entity_count"] = len(matches_dict)



# for map in map_dict:
#     # -this was for printing individual mapa data in the console-
#     # print(map)
#     # print(map_dict[map]["entity_dict"])
#     # print(map_dict[map]["entity_count"])
#     # print("----------")
#     # entity_total += map_dict[map]["entity_count"]
#     for entity in map_dict[map]["entity_dict"]:
#         if entity not in data:
#             data[entity] = map_dict[map]["entity_dict"][entity]
#         else:
#             data[entity] += map_dict[map]["entity_dict"][entity]

print(data)
make_csv_file(data)
#print(entity_total)
