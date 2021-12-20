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

positions = {0: ((0, 0, 0), tuple())}

not_done = [i for i, _ in enumerate(data) if i > 0]

tried = set()

while len(positions) < len(data):
    for i1 in not_done:
        d1 = data[i1]
        for i2 in positions:
            d2 = data[i2]
            if (i1, i2) not in tried:
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
                    c1, f1 = centres.pop()
                    c2, f2 = positions[i2]
                    positions[i1] = (add(c2, rotate(c1, f2)), (f1,) + f2)
                    not_done.remove(i1)
                    break
                else:
                    tried.add((i1, i2))
        else:
            continue
        break

def manhatten(a, b):
    return sum(abs(i - j) for i, j in zip(a, b))

largest = 0
for i, _ in positions.values():
    for j, _ in positions.values():
        largest = max(largest, manhatten(i, j))

print(largest)
