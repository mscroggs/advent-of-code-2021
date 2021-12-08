n = 0
with open("input") as f:
    for line in f:
        output = line.split("|")[1].strip()
        for digit in output.split(" "):
            if len(digit) in [2, 3, 4, 7]:
                n += 1
print(n)
