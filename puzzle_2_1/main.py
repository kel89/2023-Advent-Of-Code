possible_totals = {
    'red': 12,
    'green': 13,
    'blue': 14
}

id_sum = 0

def parse_draw(draw):
    counts = {}
    for d in draw.split(', '):
        count = d.strip().split(' ')[0]
        color = d.strip().split(' ')[1]
        counts[color] = int(count)
    return counts

def parse_game(line):
    game_id = int(line.split(":")[0].split(' ')[1])
    draws = line.split(":")[1].split(";")
    for draw in draws:
        counts = parse_draw(draw)
        for color in counts.keys():
            if counts[color] > possible_totals[color]:
                print("FALSE", line)
                return game_id, False
    return game_id, True




possible_id_total = 0
f = open("./puzzle_2_1/input.txt", "r")
for line in f:
    id, possible = parse_game(line)
    if possible:
        id_sum += id

print(id_sum)
