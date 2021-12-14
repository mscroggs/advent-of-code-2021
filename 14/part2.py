first = True
rules = {}
with open("input") as f:
    for line in f:
        if line.strip() == "":
            first = False
        elif first:
            p = line.strip()
        else:
            i, j = line.strip().split(" -> ")
            rules[i] = j

rules2 = {}
for i, j in rules.items():
    rules2[i] = [i[0] + j, j + i[1]]

pairs = {}
for i, j in zip(p, p[1:]):
    if i+j not in pairs:
        pairs[i+j] = 0
    pairs[i+j] += 1

for i in range(40):
    new_pairs = {}
    for i, j in pairs.items():
        for k in rules2[i]:
            if k not in new_pairs:
                new_pairs[k] = 0
            new_pairs[k] += j

    pairs = new_pairs

maxp = 0
minp = sum(2 * j for i, j in pairs.items())
for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    c = sum(j for i, j in pairs.items() if l == i[0]) # + sum(j for i, j in pairs.items() if l == i[1])
    if l == p[-1]:
        c += 1
    if c > 0:
        minp = min(minp, c)
        maxp = max(maxp, c)

print(maxp-minp)
