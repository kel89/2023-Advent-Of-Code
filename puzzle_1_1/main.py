import os

total = 0

def get_code(l):
    for i in l:
        if i.isdigit():
            first_number = i
            break
    for i in reversed(l):
        if i.isdigit():
            last_number = i
            break
    number = int(str(first_number) + str(last_number))
    return number

f = open("puzzle_1_1/calibration.txt", 'r')
for line in f:
    total += get_code(line)

print(total)