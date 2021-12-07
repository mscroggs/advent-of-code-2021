with open("input") as f:
    lines = [line.strip() for line in f]

oxygen = [i for i in lines]

bit = 0
while len(oxygen) > 1:
    n = len([i for i in oxygen if i[bit] == "1"])
    if n >= len(oxygen) - n:
        oxygen = [i for i in oxygen if i[bit] == "1"]
    else:
        oxygen = [i for i in oxygen if i[bit] == "0"]
    bit += 1

co2 = [i for i in lines]

bit = 0
while len(co2) > 1:
    n = len([i for i in co2 if i[bit] == "1"])
    if n < len(co2) - n:
        co2 = [i for i in co2 if i[bit] == "1"]
    else:
        co2 = [i for i in co2 if i[bit] == "0"]
    bit += 1

o_n = 0
for i, j in enumerate(oxygen[0][::-1]):
    if j == "1":
        o_n += 2 ** i

c_n = 0
for i, j in enumerate(co2[0][::-1]):
    if j == "1":
        c_n += 2 ** i

print(o_n, c_n)
print(o_n * c_n)
