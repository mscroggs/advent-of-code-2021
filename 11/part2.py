with open("input") as f:
    octs = [[int(i) for i in line] for line in f.read().strip().split("\n")]

step = 0
while True:
    step += 1
    for i, row in enumerate(octs):
        for j, o in enumerate(row):
            octs[i][j] += 1
    c = True
    f = []
    while c:
        c = False
        for i, row in enumerate(octs):
            for j, o in enumerate(row):
                if o > 9 and (i, j) not in f:
                    f.append((i, j))
                    c = True
                    for x in [i-1, i, i+1]:
                        if x >= 0 and x < len(octs):
                            for y in [j-1, j, j+1]:
                                if y >= 0 and y < len(octs[0]):
                                    print(x, y, len(octs[0]), len(octs))
                                    octs[x][y] += 1
    if len(f) == 100:
        break
    for i, j in f:
        octs[i][j] = 0

print(step)
