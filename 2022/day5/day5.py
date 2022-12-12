with open("moves.txt", "r") as f:
    moves = f.read().splitlines()

with open("stacks.txt", "r") as f:
    data = f.read()

# helpful magic
def create_stacks(data):
    stacks = data.split("\n")
    stacks.reverse()
    locations = [1, 5, 9, 13, 17, 21, 25, 29, 33]
    result = {}
    for l in locations:
        result[stacks[0][l]] = []
    
    for s in stacks[1:]:
        count = 1
        for l in locations:
            if s[l] != " ":
                result[str(count)].append(s[l])
            count += 1

    return result

def parse_moves(move):
    moves = move.split(" ")
    return int(moves[1]), moves[3], moves[5]

def move_crates(data,number,take_from,move_to):
    count = 0
    while count < number:
        if data[take_from]:
            last = data[take_from].pop(-1)
            data[move_to].append(last)
        count += 1
    return data

def move_more_crates(data,number,take_from,move_to):
    if data[take_from]:
        last = data[take_from][-number:]
        del data[take_from][-number:]
        data[move_to].extend(last)
    return data

def get_top_crates(stacks):
    top = []
    for i in stacks.keys():
        if stacks[i]:
            top.append(stacks[i][-1])
        else:
            top.append(" ")

    return "".join(top)

## Magic
stacks = create_stacks(data)
stacks2 = create_stacks(data)

for move in moves:
    number, take_from, move_to = parse_moves(move)
    # print(f"move {number}, from: {take_from}, to: {move_to}")
    stacks_round_one = move_crates(stacks,number,take_from,move_to)
    stacks_round_two = move_more_crates(stacks2,number,take_from,move_to)

print(f"Top Crates Round One: {get_top_crates(stacks_round_one)}")
print(f"Top Crates Round Two: {get_top_crates(stacks_round_two)}")