with open("input") as f:
    data = [[int(i) for i in line.strip()]for line in f]

largest_basins = [0, 0, 0]
for i, row in enumerate(data):
    for j, entry in enumerate(row):
        neighbours = []
        if i > 0:
            neighbours.append(data[i - 1][j])
        if i < len(data) - 1:
            neighbours.append(data[i + 1][j])
        if j > 0:
            neighbours.append(data[i][j - 1])
        if j < len(row) - 1:
            neighbours.append(data[i][j + 1])
        if entry < min(neighbours):
            basin = [(i, j)]
            changed = True
            while changed:
                changed = False
                for b in basin:
                    pos = []
                    if b[0] > 0:
                        pos.append((b[0] - 1, b[1]))
                    if b[0] < len(data) - 1:
                        pos.append((b[0] + 1, b[1]))
                    if b[1] > 0:
                        pos.append((b[0], b[1] - 1))
                    if b[1] < len(data) - 1:
                        pos.append((b[0], b[1] + 1))
                    for p in pos:
                        if data[p[0]][p[1]] < 9 and p not in basin:
                            changed = True
                            basin.append(p)
            print(len(basin))
            largest_basins = sorted(largest_basins + [len(basin)])[1:]
print(largest_basins[0] * largest_basins[1] * largest_basins[2])
