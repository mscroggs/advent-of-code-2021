with open("input") as f:
    positions = [int(line.split(":")[1]) for line in f]

scores = [0, 0]

next = 0
rolls = 0
def die():
    global next
    global rolls
    rolls += 1
    next += 1
    if next > 100:
        next -= 100
    return next

turn = 0
while max(scores) < 1000:
    for i in range(3):
        positions[turn] += die()
    while positions[turn] > 10:
        positions[turn] -= 10
    scores[turn] += positions[turn]
    turn = 1 - turn

print(rolls * min(scores))
