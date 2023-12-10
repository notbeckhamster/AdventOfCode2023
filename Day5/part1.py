file = open("Day5/input.txt")
line_list = file.readlines()
seeds_list = line_list[0].strip().split(" ")[1:]
maps_list = line_list[2:]
maps_list_filter = [x.replace("\n","") for x in maps_list]
maps_list_num = [x for x in maps_list_filter if len(x)>0]
#Loop through maps.. 
list_idx_used = []
for each_map in maps_list_num:
    #Loop through seeds 
    if ("map" in each_map):
        list_idx_used = []
        continue
    #split each_map
    split_map = each_map.split(" ")
    for idx, each_seed_val in enumerate(seeds_list):
        if idx not in list_idx_used and int(each_seed_val) < (int(split_map[1]) + int(split_map[2])) and int(each_seed_val) >= int(split_map[1]):
            dif = int(split_map[0])-int(split_map[1])
            seeds_list[idx] = int(each_seed_val) + dif
            list_idx_used.append(idx)
print(seeds_list)
print(min(seeds_list))