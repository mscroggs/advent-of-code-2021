with open("input") as f:
    data = [int(line) for line in f]

prev = None
count = 0

for i, j, k in zip(data, data[1:], data[2:]):
    n = i + j + k
    if prev is not None and n > prev:
        count += 1
    prev = n

print(count)
