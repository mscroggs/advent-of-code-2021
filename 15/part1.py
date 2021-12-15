costs = {}
M = 0
with open("input") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            costs[(i, j)] = int(c)
            M += int(c)
x = max(i for i, j in costs) + 1
y = max(j for i, j in costs) + 1

todo = {i for i in costs}

scores = {i: M for i in costs}
scores[(x-1, y-1)] = costs[(x-1,y-1)]

while len(todo) > 0:
    next = (None, M)
    for i in todo:
        if scores[i] < next[1]:
            next = (i, scores[i])
    todo.remove(next[0])
    nx, ny = next[0]
    for a, b in [(nx - 1, ny), (nx + 1, ny), (nx, ny - 1), (nx, ny + 1)]:
        if (a, b) in todo:
            scores[(a, b)] = min(scores[(a, b)], next[1] + costs[(a, b)])

print(scores[(0,0)] - costs[(0,0)])
