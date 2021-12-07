position = [0, 0]

with open("input") as f:
    for line in f:
        d, n = line.split(" ")
        n = int(n)
        if d == "up":
            position[1] -= n
        elif d == "down":
            position[1] += n
        elif d == "forward":
            position[0] += n
        else:
            raise ValueError

print(position[0] * position[1])

