
max_cubes = {"red":12, "green": 13, "blue":14}

if __name__ == "__main__":
    sum_id = 0
    file = open("Day2/input.txt", "r")
    for line in file: 
        #Track id from char 5 to index of : exclusive
        id = int(line[5:line.index(":")])
        game_data = line[line.index(":")+2:]
        game_data = game_data.replace("\n", "")
        game_data_list = game_data.split("; ")
        #track # of cubes 
        max_num_cube_per_game = {"red": 0, "blue": 0, "green": 0}
        for turn in game_data_list:
            num_cubes = {"red": 0, "blue": 0, "green":0}
            turn_list = turn.split(", ")
            for grab in turn_list:
                grab_list = grab.split(" ")
                num_cube_in_grab = int(grab_list[0])
                num_cubes[grab_list[1]] += num_cube_in_grab
            for color in num_cubes.keys():
                if num_cubes[color] > max_num_cube_per_game[color]: max_num_cube_per_game[color] = num_cubes[color]
        if_valid = True
        for color in num_cubes.keys():
            if max_num_cube_per_game[color]>max_cubes[color]: if_valid=False
        if if_valid == True: 
            sum_id+=id
            print(id)
    print(sum_id)
        #note down the # of cubes
