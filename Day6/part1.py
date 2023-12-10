file = open("Day6/input.txt")
file_list = file.readlines()
time_list = file_list[0][6:].strip().split(" ")
time_list = [x for x in time_list if x != ""]
dist_list = file_list[1][9:].strip().split(" ")
dist_list = [x for x in dist_list if x != ""]
print(time_list)
print(dist_list)
len_of_winning_times_list = []
for idx, time in enumerate(time_list):
    dist = int(dist_list[idx])
    winning_times_list = []
    for x in range(1, int(time)):
        time_left = int(time)-x
        dist_travelled = time_left*x 
        if dist_travelled > dist: winning_times_list.append(int(time))
    len_of_winning_times_list.append(len(winning_times_list))

sum = 1
for x in len_of_winning_times_list:
    sum*=x
print(sum)