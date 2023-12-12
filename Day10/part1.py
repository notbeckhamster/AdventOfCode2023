file = open("Day10/input.txt")
file_lines = []
for each_line in file:
    file_lines.append(list(map(int, each_line.split(" "))))

sum=0
for curr_list in file_lines:
    diff_list = []
    diff_list.append(curr_list)
    while any(element != 0 for element in curr_list):
        temp_list = []
        for idx in range(0, len(curr_list)-1):
            temp_list.append(curr_list[idx+1]-curr_list[idx])
        curr_list = temp_list
        diff_list.append(curr_list)
    print(diff_list)
    ## append 0 to end of diff
    diff_list[len(diff_list)-1].append(0)
    for idx in range(len(diff_list)-1, 0, -1):
        diff_list[idx-1].append(diff_list[idx][-1] + diff_list[idx-1][-1])
    print(diff_list[0][-1])
    sum += diff_list[0][-1]
print(sum)