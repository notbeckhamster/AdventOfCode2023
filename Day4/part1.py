import re
input = open("Day4/input.txt")
input_list = input.readlines()
win_num_list = []
for idx, line in enumerate(input_list):
    win_num_list.append(line[line.index(":")+1:-1].split("|"))
    win_num_list[idx][0]=  win_num_list[idx][0].strip()
    win_num_list[idx][1]=  win_num_list[idx][1].strip()
sum = 0
for idx, line in enumerate(win_num_list):
    numbers_you_have_list = [each for each in line[1].split(" ") if each.isdigit()]
    winning_numbers_list = [each for each in line[0].split(" ") if each.isdigit()]
    intersection_list = [each for each in numbers_you_have_list if each in winning_numbers_list]
    if len(intersection_list) != 0: sum += 2**(len(intersection_list)-1)
    
    
            
print(sum)