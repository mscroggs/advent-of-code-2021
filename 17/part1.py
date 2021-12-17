with open("input") as f:
    data = f.read()
    x = [int(i) for i in data.split("x=")[1].split(",")[0].split("..")]
    y = [int(i) for i in data.split("y=")[1].split("..")]

def works(i, j):
    highest = 0
    pos = [0, 0]
    while pos[0] <= x[1] and pos[1] >= y[0]:
        highest = max(highest, pos[1])
        if x[0] <= pos[0] <= x[1] and y[0] <= pos[1] <= y[1]:
            return True, highest
        pos[0] += i
        pos[1] += j
        if i > 0:
            i -= 1
        elif i < 0:
            i += 1
        j -= 1
    return False, None

highest = 0

for n in range(1, 200):
    for i in range(min(n + 1, x[1] + 1)):
        j = n - i
        a, h = works(i, j)
        if a:
            highest = max(highest, h)
print(highest)
