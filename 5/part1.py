points = {}

with open("input") as f:
    for line in f:
        a, b = line.split(" -> ")
        x1, y1 = [int(i) for i in a.split(",")]
        x2, y2 = [int(i) for i in b.split(",")]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, y) not in points:
                    points[(x1, y)] = 0
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if (x, y1) not in points:
                    points[(x, y1)] = 0
                points[(x, y1)] += 1
        else:
            print(x1, y1, x2, y2)

print(len([i for i in points.values() if i > 1]))
