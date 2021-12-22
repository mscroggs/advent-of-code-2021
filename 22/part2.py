def collide(a, b):
    if a[0][1] < b[0][0] or b[0][1] < a[0][0]:
        return False
    if a[1][1] < b[1][0] or b[1][1] < a[1][0]:
        return False
    if a[2][1] < b[2][0] or b[2][1] < a[2][0]:
        return False
    return True

def to_tuple(a):
    return tuple(tuple(i) for i in a)

def remove(a, b):
    """Remove parts of cuboid b from cubiod a."""
    out = []
    a = [[j for j in i] for i in a]
    if a[0][0] < b[0][0]:
        out.append(to_tuple([[a[0][0], b[0][0] - 1], a[1], a[2]]))
        a[0][0] = b[0][0]
    if a[0][1] > b[0][1]:
        out.append(to_tuple([[b[0][1] + 1, a[0][1]], a[1], a[2]]))
        a[0][1] = b[0][1]
    if a[1][0] < b[1][0]:
        out.append(to_tuple([a[0], [a[1][0], b[1][0] - 1], a[2]]))
        a[1][0] = b[1][0]
    if a[1][1] > b[1][1]:
        out.append(to_tuple([a[0], [b[1][1] + 1, a[1][1]], a[2]]))
        a[1][1] = b[1][1]
    if a[2][0] < b[2][0]:
        out.append(to_tuple([a[0], a[1], [a[2][0], b[2][0] - 1]]))
        a[2][0] = b[2][0]
    if a[2][1] > b[2][1]:
        out.append(to_tuple([a[0], a[1], [b[2][1] + 1, a[2][1]]]))
        a[2][1] = b[2][1]
    return out

data = []
with open("input") as f:
    for line in f:
        status, points = line.split(" ")
        points = points.split(",")
        lims = [[int(i) for i in p.split("=")[1].split("..")]
                for p in points]
        data.append((status, lims))

on = set()
cuboids = []
for status, cuboid in data:
    new_cuboids = []
    for c in cuboids:
        if collide(c, cuboid):
            new_cuboids += remove(c, cuboid)
        else:
            new_cuboids.append(c)
    if status == "on":
        new_cuboids.append(cuboid)
    cuboids = new_cuboids

size = 0
for c in cuboids:
    size += (1 + c[0][1] - c[0][0]) * (1 + c[1][1] - c[1][0]) * (1 + c[2][1] - c[2][0])
print(size)
