ones = None
count = 0

with open("input") as f:
    for line in f:
        if ones is None:
            ones = [0 for i in line.strip()]
        for i, j in enumerate(line.strip()):
            if j == "1":
                ones[i] += 1
        count += 1


gamma = 0
eps = 0
for i, j in enumerate(ones[::-1]):
    if j > count / 2:
        gamma += 2 ** i
    else:
        eps += 2 ** i

print(gamma * eps)
