

def get_first_digit(string: str) -> int:
    for x in string:
        if x.isdigit(): return x

def get_last_digit(string: str) -> int:
    for idx in range(len(string)-1, -1, -1):
        if string[idx].isdigit(): return string[idx]

def get_cali_value(string: str) -> int:
    return int(get_first_digit(string) + get_last_digit(string))

if  __name__ == "__main__":
    print(get_cali_value("1abc2"))
    print(get_cali_value("pqr3stu8vwx"))
    print(get_cali_value("a1b2c3d4e5f"))
    print(get_cali_value("treb7uchet"))