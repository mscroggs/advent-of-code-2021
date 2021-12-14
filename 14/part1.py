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

for i in range(10):
    new_p = ""
    for i, j in zip(p, p[1:]):
        new_p += i
        if i + j in rules:
            new_p += rules[i + j]
    new_p += p[-1]
    p = new_p

minp = len(p)
maxp = 0
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if i in p:
        minp = min(minp, p.count(i))
        maxp = max(maxp, p.count(i))

print(maxp - minp)
