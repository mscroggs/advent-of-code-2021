prev = None
count = 0

with open("input") as f:
    for line in f:
        n = int(line)
        if prev is not None and n > prev:
            count += 1
        prev = n

print(count)
