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

f = folds[0]

if f[0] == "x":
    newdots = set()
    for d in dots:
        if d[0] == f[1]:
            raise ValueError
        elif d[0] > f[1]:
            newdots.add((f[1] - (d[0] - f[1]), d[1]))
        else:
            newdots.add(d)
    dots = newdots

print(len(dots))
