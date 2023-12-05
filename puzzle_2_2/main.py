


def parse_draw(draw, min_possible):
    for d in draw.split(', '):
        count = int(d.strip().split(' ')[0])
        color = d.strip().split(' ')[1]
        if min_possible[color] < count:
            min_possible[color] = count
    return min_possible

def get_game_power(line):
    game_id = int(line.split(":")[0].split(' ')[1])
    draws = line.split(":")[1].split(";")
    min_possible = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for draw in draws:
        min_possible = parse_draw(draw, min_possible)
    power = 1
    print(min_possible.values())
    for val in min_possible.values():
        power = power * val

    print(min_possible)
    print(line)
    print("Power", power)
    print("-"*50)
    return power


powers  =[]
for line in open("./puzzle_2_2/input.txt", "r"):
    powers.append(get_game_power(line))

print(sum(powers))