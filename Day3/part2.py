import re 
input = open("Day3/input.txt")

input_list = input.readlines()
print(len(input_list))
print(len(input_list[0]))
number_dict = {}
sum=0
#Find all numbers
for row, line in enumerate(input_list):
    for each_symbol_find in re.finditer("\d+", line):
        for idx in range(each_symbol_find.end()-each_symbol_find.start()):
            number_dict[(row, each_symbol_find.start()+idx)] = each_symbol_find.group()
#Iterate around symbols to locate numbers and add them
for row, line in enumerate(input_list):
    for num in re.finditer("\*", line):
        #iterate around number to chekc for symbols
        two_num = [0,0]
        for row_search in range(row-1, row+2):
            for col_search in range(num.start()-1, num.end()+1):
                if two_num[0] == 0 and (row_search, col_search) in number_dict.keys():
                    two_num[0] = number_dict[(row_search, col_search)]
                    continue
                if two_num[1] == 0 and (row_search, col_search) in number_dict.keys():
                    if number_dict[(row_search, col_search)] != two_num[0]:
                        two_num[1] = number_dict[(row_search, col_search)]

        print(two_num)
        sum+=(int(two_num[0])*int(two_num[1]))
print(sum)