data = []

with open("input") as f:
    for line in f:
        if line.startswith("---"):
            data.append([])
        elif line.strip() != "":
            data[-1].append(tuple(int(i) for i in line.split(",")))

rotations = [lambda x, y, z: (x, y, z),
             lambda x, y, z: (x, z, -y),
             lambda x, y, z: (x, -y, -z),
             lambda x, y, z: (x, -z, y),
             lambda x, y, z: (-x, -y, z),
             lambda x, y, z: (-x, z, y),
             lambda x, y, z: (-x, y, -z),
             lambda x, y, z: (-x, -z, -y),
             lambda x, y, z: (y, -x, z),
             lambda x, y, z: (y, z, x),
             lambda x, y, z: (y, x, -z),
             lambda x, y, z: (y, -z, -x),
             lambda x, y, z: (-y, z, -x),
             lambda x, y, z: (-y, -x, -z),
             lambda x, y, z: (-y, -z, x),
             lambda x, y, z: (-y, x, z),
             lambda x, y, z: (z, x, y),
             lambda x, y, z: (z, y, -x),
             lambda x, y, z: (z, -x, -y),
             lambda x, y, z: (z, -y, x),
             lambda x, y, z: (-z, -x, y),
             lambda x, y, z: (-z, y, x),
             lambda x, y, z: (-z, x, -y),
             lambda x, y, z: (-z, -y, -x)]
inv_rotations = [lambda x, y, z: (x, y, z),
                 lambda x, z, y: (x, -y, z),
                 lambda x, y, z: (x, -y, -z),
                 lambda x, z, y: (x, y, -z),
                 lambda x, y, z: (-x, -y, z),
                 lambda x, z, y: (-x, y, z),
                 lambda x, y, z: (-x, y, -z),
                 lambda x, z, y: (-x, -y, -z),
                 lambda y, x, z: (-x, y, z),
                 lambda y, z, x: (x, y, z),
                 lambda y, x, z: (x, y, -z),
                 lambda y, z, x: (-x, y, -z),
                 lambda y, z, x: (-x, -y, z),
                 lambda y, x, z: (-x, -y, -z),
                 lambda y, z, x: (x, -y, -z),
                 lambda y, x, z: (x, -y, z),
                 lambda z, x, y: (x, y, z),
                 lambda z, y, x: (-x, y, z),
                 lambda z, x, y: (-x, -y, z),
                 lambda z, y, x: (x, -y, z),
                 lambda z, x, y: (-x, y, -z),
                 lambda z, y, x: (x, y, -z),
                 lambda z, x, y: (x, -y, -z),
                 lambda z, y, x: (-x, -y, -z)]

def rotate(points, rot):
    return [rot(*p) for p in points]

def relative(points, p):
    return [sub(q, p) for q in points]

def sub(p, q):
    return tuple(i - j for i, j in zip(p, q))

def add(p, q):
    return tuple(i + j for i, j in zip(p, q))

def map_to(points, a, b):
    return [sub(p, sub(a, b)) for p in points]

def norm(p):
    return max(abs(i) for i in p)

def rotate(point, ls):
    out = tuple(i for i in point)
    for i in ls:
        out = rotations[i](*out)
    return out

relatives = {}

for i1, d1 in enumerate(data):
    for i2, d2 in enumerate(data):
        if i1 != i2:
            possible_cs = set(
                (sub(q, r(*p)), r_n)
                for p in d1 for q in d2 for r_n, r in enumerate(rotations))
            centres = set()
            for c, r_n in possible_cs:
                r = rotations[r_n]
                rotated = [add(c, r(*pt)) for pt in d1]

                overlaps = set(pt for pt in rotated if norm(pt) <= 1000)
                overlaps2 = set(pt for pt in d2 if norm(sub(pt, c)) <= 1000)

                if len(overlaps) >= 12 and overlaps == overlaps2:
                    centres.add((c, r_n))
            if len(centres) == 1:
                print(i1, i2, centres)
                relatives[(i2, i1)] = centres.pop()

positions = {0: ((0, 0, 0), tuple())}

while len(positions) < len(data):
    for a, b in relatives:
        if a in positions and b not in positions:
            print(a, b)
            c1, f1 = relatives[(a, b)]
            c2, f2 = positions[a]

            positions[b] = (add(c2, rotate(c1, f2)), (f1,) + f2)

            break

beacons = set()
for i, (c, f) in positions.items():
    for p in data[i]:
        beacons.add(add(c, rotate(p, f)))

print(len(beacons))
