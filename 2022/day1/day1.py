# https://adventofcode.com/2022/day/1

with open("day1.txt", "r") as f:
    data = f.read().splitlines()

elves = []
count = 0 
elf = 1
for d in data:
    if d:
        count += int(d)
    else:
        elves.append({"elf": elf, "calories": count})
        count = 0
        elf += 1
        continue

max_calories = max(elves, key=lambda x:x['calories'])
print(f"Elf {max_calories['elf']} has the most with {max_calories['calories']}")

fat_elves = sorted(elves, key=lambda x:x['calories'], reverse=True)[:3] 
total = sum(x["calories"] for x in fat_elves)
print(f"Total calories for the top 3 Elves: {total}")