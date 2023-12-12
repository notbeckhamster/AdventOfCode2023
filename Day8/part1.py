file = open("Day8/input.txt")
file_lines = file.readlines()
direction = file_lines[0].strip()
maps = [each_line.strip() for each_line in file_lines[2:]]
print(direction)
print(maps)
#form dict with map 
map_dict = {}
for each_keyval in maps:
    key = each_keyval[0:3]
    val = (each_keyval[-9:-6], each_keyval[-4:-1])
    map_dict[key] = val
#convert LRLRLR string to 0's and 1's
direction_num = ""
for each_char in direction:
    if each_char == "L":
        direction_num += "0"
    else:
        direction_num += "1"

#Loop through 
curr_key = 'AAA'
count = 0
while (curr_key != 'ZZZ'):
    for direction in direction_num:
        curr_key = map_dict[curr_key][int(direction)]
        count+=1
print(count)
