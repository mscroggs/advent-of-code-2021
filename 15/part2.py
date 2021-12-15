inputcosts = {}
with open("input") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            inputcosts[(i, j)] = int(c)

x = max(i for i, j in inputcosts) + 1
y = max(j for i, j in inputcosts) + 1

costs = {}
for i in range(5):
    for j in range(5):
        for (a, b), c in inputcosts.items():
            costs[(x*i + a, y*j + b)] = 1 + (c + i + j - 1) % 9

M = sum(costs.values())

x = max(i for i, j in costs) + 1
y = max(j for i, j in costs) + 1

size = 0
while size != len(costs):
    size = len(costs)
    for i in range(x):
        for j in range(y):
            if (i, j) in costs and (i + 1, j) not in costs and (i, j - 1) not in costs and costs[(i - 1, j + 1)] < costs[(i, j)]:
                del costs[(i, j)]


todo = {i for i in costs}
todo2 = {(x-1,y-1)}

scores = {i: M for i in costs}
scores[(x-1, y-1)] = costs[(x-1,y-1)]

while (0,0) in todo:
    next = (None, M)
    for i in todo2:
        if scores[i] < next[1]:
            next = (i, scores[i])
    todo.remove(next[0])
    todo2.remove(next[0])
    nx, ny = next[0]
    for a, b in [(nx - 1, ny), (nx + 1, ny), (nx, ny - 1), (nx, ny + 1)]:
        if (a, b) in todo:
            scores[(a, b)] = min(scores[(a, b)], next[1] + costs[(a, b)])
            todo2.add((a,b))

    print(len(todo))

print(scores[(0,0)] - costs[(0,0)])
