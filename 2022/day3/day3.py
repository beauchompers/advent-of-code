with open("day3.txt", "r") as f:
    data = f.read().splitlines()

# To help prioritize item rearrangement, every item type can be converted to a priority:

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

def get_values(items):
    total = 0
    for i in items:
        if i.isupper():
            total += ord(i.lower()) - 96 + 26
        else:
            total += ord(i.lower()) - 96
    return total

def get_same_items(first, second):
    matches = [ x for x in first if x in second]
    return list(set(matches))

def get_same_group_items(first, second, third):
    matches = [ x for x in first if x in second and x in third]
    return list(set(matches))

# first park
total = 0
for d in data:
    first, second = list(map(str,d[:len(d)//2])), list(map(str,d[len(d)//2:]))
    matches = get_same_items(first,second)
    total += get_values(matches)

print(total)

#second part
start = 0
end = 3
group_total = 0
count = 0

while start < len(data):
    group_pack = data[start:end]
    matches = get_same_group_items(list(map(str, group_pack[0])),list(map(str, group_pack[1])),list(map(str, group_pack[2])))
    group_total += get_values(matches)
    start += 3
    end += 3

print(group_total)