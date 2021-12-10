with open("input") as f:
    data = [[int(i) for i in line.strip()]for line in f]

out = 0
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
            out += entry + 1
print(out)
