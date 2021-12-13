dotmode = True
dots = set()
folds = []

with open("input") as f:
    for line in f:
        if line.strip() == "":
            dotmode = False
        elif dotmode:
            dots.add(tuple(int(i) for i in line.split(",")))
        else:
            i, j = line.strip().split(" ")[-1].split("=")
            folds.append((i, int(j)))

for f in folds:
    newdots = set()
    if f[0] == "x":
        for d in dots:
            if d[0] == f[1]:
                raise ValueError
            elif d[0] > f[1]:
                newdots.add((f[1] - (d[0] - f[1]), d[1]))
            else:
                newdots.add(d)
    else:
        assert f[0] == "y"
        for d in dots:
            if d[1] == f[1]:
                raise ValueError
            elif d[1] > f[1]:
                newdots.add((d[0], f[1] - (d[1] - f[1])))
            else:
                newdots.add(d)
    dots = newdots

xmax = max(i[0] for i in dots)
ymax = max(i[1] for i in dots)

for i in range(ymax + 1):
    print("".join("#" if (j, i) in dots else " " for j in range(xmax + 1)))
