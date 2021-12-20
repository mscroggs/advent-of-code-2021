first = True

data = []

with open("input") as f:
    for line in f:
        if first:
            decode = "".join(["1" if i == "#" else "0" for i in line.strip()])
            first = False
        elif line.strip() != "":
            data.append("".join(["1" if i == "#" else "0" for i in line.strip()]))

def get(data, i, j, default):
    if (i, j) not in data:
        return default
    return data[(i, j)]

def bin2dec(n):
    return sum(2**i for i, j in enumerate(n[::-1]) if j == "1")

shape = (-51, len(data) + 52, -51, len(data[0]) + 52)

data = {(i, j): entry for i, row in enumerate(data) for j, entry in enumerate(row)}

default = "0"
for _ in range(50):
    print(_, default)
    image = {}
    irange = (min(i[0] for i in data) - 2, max(i[0] for i in data) + 3)
    jrange = (min(i[1] for i in data) - 2, max(i[1] for i in data) + 3)
    for i in range(*irange):
        for j in range(*jrange):
            n = get(data, i - 1, j - 1, default) + get(data, i - 1, j, default) + get(data, i - 1, j + 1, default)
            n += get(data, i, j - 1, default) + get(data, i, j, default) + get(data, i, j + 1, default)
            n += get(data, i + 1, j - 1, default) + get(data, i + 1, j, default) + get(data, i + 1, j + 1, default)
            n = bin2dec(n)
            image[(i, j)] = decode[n]

    data = image

    if default == "0":
        default = decode[0]
    else:
        default = decode[-1]

print([data[i, j] for i in range(shape[0], shape[1]) for j in range(shape[2], shape[3])].count("1"))
