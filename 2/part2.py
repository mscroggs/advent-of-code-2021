position = [0, 0]
aim = 0

with open("input") as f:
    for line in f:
        d, n = line.split(" ")
        n = int(n)
        if d == "up":
            aim -= n
        elif d == "down":
            aim += n
        elif d == "forward":
            position[0] += n
            position[1] += aim * n
        else:
            raise ValueError

print(position[0] * position[1])

