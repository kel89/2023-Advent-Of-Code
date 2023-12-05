# Get all the card data
f = open("./puzzle_4_1/input.txt", 'r')
i = 1
card_dict = {}
for l in f:
    card_dict[i] = l
    i += 1

def card_value(l):
    card_id = int(l.split(":")[0].split(" ")[-1])
    [winning_nums, my_nums] = l.split(":")[1].strip().split("|")
    winning_nums = [int(x) for x in winning_nums.strip().split(' ') if x != ''] 
    my_nums = [int(x) for x in my_nums.strip().split(' ') if x != '']
    overlap = 0
    for x in my_nums:
        if x in winning_nums:
            overlap += 1
    if overlap == 0:
        return 0
    return 2**(overlap - 1)


saved = {}


def process_card(card_id):
    if card_id in saved.keys():
        return saved[card_id]
    
    card = card_dict[card_id]
    [winning_nums, my_nums] = card.split(":")[1].strip().split("|")
    winning_nums = [int(x) for x in winning_nums.strip().split(' ') if x != ''] 
    my_nums = [int(x) for x in my_nums.strip().split(' ') if x != '']
    overlap = 0
    for x in my_nums:
        if x in winning_nums:
            overlap += 1
    if overlap == 0:
        return 0, []
    
    saved[card_id] = (overlap, list(range(card_id + 1, card_id+1+overlap)))
    return (overlap, list(range(card_id + 1, card_id+1+overlap)))



cards = list(range(1, len(card_dict.keys())+1))
won_cards = []
count = len(card_dict.keys())
multiplier = {i: 1 for i in range(1, len(card_dict.keys())+1)}
while len(cards) > 0:
    # print(len(cards))
    card = cards.pop(0)
    (count_won, new_cards) = process_card(card)
    count += count_won
    won_cards = won_cards + new_cards
    cards.sort()
print(count)