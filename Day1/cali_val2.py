str_to_work_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def eval_idx(string: str, idx: int) -> str:
    char_at_idx = string[idx]
    if char_at_idx.isdigit(): return char_at_idx
    #take slices len 3,4,5 check against map keys
    for length in range(3, 6, 1):
        if (idx+length <= len(string)):
            if (string[idx:idx+length] in str_to_work_map.keys()):
                return str_to_work_map[string[idx:idx+length]] 

def get_first_digit(string: str) -> str:
    for idx, x in enumerate(string):
        result = eval_idx(string, idx)
        if (result != None): return result

def get_last_digit(string: str) -> str:
    for idx in range(len(string)-1, -1, -1):
        result = eval_idx(string, idx)
        if (result != None): return result 

def get_cali_value(string: str) -> int:
    return int(get_first_digit(string) + get_last_digit(string))

if  __name__ == "__main__":
    strings = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

    for s in strings:
        result = get_cali_value(s)
        print(f"Value: {result}")