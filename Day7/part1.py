from collections import Counter
from functools import cmp_to_key
type_list = [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3), (2,3), (1,4), (5,)]
file = open("Day7/input.txt")
file_lines = file.readlines()
card_order = "23456789TJQKA"
def compare_hand_types(hand1: tuple, hand2: tuple) -> int:
    hand1_card = hand1[0]
    hand2_card = hand2[0]
    hand1_counter = Counter(hand1_card)
    hand2_counter = Counter(hand2_card)
    hand1_type = tuple(sorted(hand1_counter.values()))
    hand2_type = tuple(sorted(hand2_counter.values()))
    print(f'{hand1_card} {hand1_type} {hand1_counter.values()}')
    print(f'{hand2_card} {hand2_type}')
    type_dif =type_list.index(hand1_type)-type_list.index(hand2_type)
    #same type perform check of each digit
    if type_dif == 0:
        for idx in range(0, len(hand1_card)):
            dif = card_order.index(hand1_card[idx]) - card_order.index(hand2_card[idx])
            if dif != 0: return dif
    
    return type_list.index(tuple(hand1_type))-type_list.index(tuple(hand2_type))

list_split = []
for each_line in file_lines:
    #split line 
    split_line = each_line.strip().split(" ")
    hand = split_line[0].strip()
    bet = split_line[1].strip()
    list_split.append((hand, bet))
sorted_hands = sorted(list_split, key=cmp_to_key(compare_hand_types))
sum = 0
for idx, each_hand in enumerate(sorted_hands):
    sum += (idx+1)*int(each_hand[1])
print(sum)
    




