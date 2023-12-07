import re 
input = open("Day3/input.txt")

input_list = input.readlines()
print(len(input_list))
print(len(input_list[0]))
symbol_list = []
sum=0
#Find all symbols
for row, line in enumerate(input_list):
    for each_symbol_find in re.finditer("[^\d.\n]", line):
        symbol_list.append((row, each_symbol_find.start()))
#Iterate around symbols to locate numbers and add them
for row, line in enumerate(input_list):
    for num in re.finditer("\d+", line):
        #iterate around number to chekc for symbols
        if_found = False
        for row_search in range(row-1, row+2):
            for col_search in range(num.start()-1, num.end()+1):
                if if_found == False and (row_search, col_search) in symbol_list:
                    if_found = True
                    sum+=int(num.group())

print(sum)