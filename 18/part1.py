import json

fish = []
with open("input") as f:
    for line in f:
        fish.append(json.loads(line))

def reformat(f, level=0):
    out = []
    for i in f:
        if isinstance(i, list):
            out += reformat(i, level + 1)
        else:
            out.append([i, level])
    return out

fish = [reformat(f) for f in fish]

def explode(a):
    for n, (i, j) in enumerate(a):
        if j == 4:
            out = a[:n]
            if len(out) > 0:
                out[-1][0] += a[n][0]
            out.append([0, 3])
            if len(a[n+2:]) > 0:
                out.append([a[n+1][0] + a[n+2][0], a[n+2][1]])
            out += a[n+3:]
            return explode(out)
    for n, (i, j) in enumerate(a):
        if i >= 10:
            out = a[:n]
            out += [[i // 2, j + 1], [(i + 1) // 2, j + 1]]
            out += a[n+1:]
            return explode(out)
    return a

def add(a, b):
    out = [[i, j + 1] for i, j in a + b]
    while True:
        out = explode(out)
        break
    return out

def magnitude(a):
    if len(a) == 1:
        return a[0][0]
    for n, (i, j) in enumerate(a):
        if n + 1 < len(a) and a[n+1][1] == j:
            return magnitude(a[:n] + [[3 * i + 2 * a[n+1][0], j - 1]] + a[n+2:])
    for n, (i, j) in enumerate(a):
        if (n == 0 or a[n-1][1] < j) and (n == len(a) - 1 or a[n+1][1] < j):
            return magnitude(a[:n] + [[i, j - 1]] + a[n+1:])

result = fish[0]
for f in fish[1:]:
    result = add(result, f)

print(magnitude(result))

