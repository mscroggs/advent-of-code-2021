with open("input") as f:
    positions = [int(i) for i in f.read().split(",")]

mincost = max(positions) * len(positions)
for p in range(min(positions), max(positions)):
    cost = sum(abs(i - p) for i in positions)
    if cost < mincost:
        mincost = cost

print(mincost)
