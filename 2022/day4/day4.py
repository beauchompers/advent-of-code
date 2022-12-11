
with open("day4.txt", "r") as f:
    data = f.read().splitlines()

def generate_range(group):
    groups = group.split("-")
    return [ x for x in list(range(int(groups[0]),int(groups[1])+1)) ]

matches = 0
overlap = 0
for d in data:
    groups = d.split(",")
    first_group = generate_range(groups[0])
    second_group = generate_range(groups[1])

    if all(x in first_group for x in second_group):
        matches += 1
    elif all(x in second_group for x in first_group):
        matches += 1
 
    if any(x in first_group for x in second_group):
        overlap += 1
    elif any(x in second_group for x in first_group):
        overlap += 1

print(matches)
print(overlap)

