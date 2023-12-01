

numbers = [
    # "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

mapping ={
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4, 
    "five": 5, 
    "six": 6,
    "seven": 7,
    "eight": 8, 
    "nine": 9
}


def get_first_number(line):
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]
        for num in numbers:
            target_len =len(num)
            if line[i: i + target_len] == num:
                return num


def get_last_number(line):
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            return line[i]
        for num in numbers:
            target_len =len(num)
            if line[i: i + target_len] == num:
                return num


def get_value(line):
    first = get_first_number(line)
    last = get_last_number(line)

    if first.isdigit():
        first_digit = first
    else:
        first_digit = mapping[first]
    
    if last.isdigit():
        last_digit = last
    else:
        last_digit = mapping[last]
    code = int(str(first_digit) + str(last_digit))
    return code





total = 0
f =open ("puzzle_1_2/calibration.txt", "r")
for line in f:
    total += get_value(line)

print(total)