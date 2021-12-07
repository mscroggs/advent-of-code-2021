with open("input") as f:
    positions = [int(i) for i in f.read().split(",")]

def triangle(n):
    return n * (n + 1) // 2

mincost = max(positions) ** 2 * len(positions)
for p in range(min(positions), max(positions)):
    cost = sum(triangle(abs(i - p)) for i in positions)
    if cost < mincost:
        mincost = cost

print(mincost)
