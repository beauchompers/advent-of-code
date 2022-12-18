import numpy

with open("day8.txt", "r") as f:
    data = f.read().splitlines()

grid = numpy.zeros((len(data), len(data[0])), dtype=int)
for x, line in enumerate(data):
    grid[x, :] = numpy.array(list(line))

## PART 1
external = (len(data[0]) * 2) + (len(data) - 2) * 2
internal = 0
for x in range(1, grid.shape[0]-1):
    for y in range(1, grid.shape[1]-1):
        tree = grid[x,y]
        # print(tree)
        grid_column = grid[:, y] 
        grid_row = grid[x, :]
        # left - right - top - bottom
        trees = [max(grid_row[:y]), max(grid_row[y+1:]), max(grid_column[:x]),max(grid_column[x+1:])]
        visible = False
        for t in trees:
            if tree > t:
                visible = True
        if visible:
            internal += 1

print(f"Total Trees Visible: {external + internal}")

## Part 2
all_scores = []
for x in range(1, grid.shape[0]-1):
    for y in range(1, grid.shape[1]-1):
        tree = grid[x,y]
        grid_column = grid[:, y] 
        grid_row = grid[x, :]
        # left - right - top - bottom
        trees = [grid_row[y-1::-1], grid_row[y+1:], grid_column[x-1::-1],grid_column[x+1:]]

        scores = []
        for t in trees:
            score = 0
            for tt in t:
                if tree == tt:
                    score += 1
                    break
                if tree > tt:
                    score += 1
                if tt > tree:
                    score += 1
                    break
        
            scores.append(score)
            all_scores.append(numpy.prod(scores))
           
print(f"Best Score: {max(all_scores)}")