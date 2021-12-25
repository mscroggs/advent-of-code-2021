positions = {}
size = [0, 0]
with open("input") as f:
    for i, line in enumerate(f):
        size[0] = max(i, size[0])
        for j, c in enumerate(line.strip()):
            size[1] = max(j, size[1])
            if c != ".":
                positions[(i, j)] = c

steps = 0
changed = True
while changed:
    changed = False
    new_positions = {}
    for (y, x), j in positions.items():
        if j == ">":
            if x < size[1] and (y, x + 1) not in positions:
                new_positions[(y, x+1)] = ">"
                changed = True
            elif x == size[1] and (y, 0) not in positions:
                new_positions[(y, 0)] = ">"
                changed = True
            else:
                new_positions[(y, x)] = ">"
        else:
            new_positions[(y, x)] = "v"
    positions = new_positions
    new_positions = {}
    for (y, x), j in positions.items():
        if j == "v":
            if y < size[0] and (y + 1, x) not in positions:
                new_positions[(y+1, x)] = "v"
                changed = True
            elif y == size[0] and (0, x) not in positions:
                new_positions[(0, x)] = "v"
                changed = True
            else:
                new_positions[(y, x)] = "v"
        else:
            new_positions[(y, x)] = ">"
    positions = new_positions
    steps += 1
    # for y in range(size[0] + 1):
    #    print("".join([positions[(y, x)] if (y, x) in positions else "." for x in range(size[1] + 1)]))

print(steps)
