from itertools import product

numbers = {0: "abcefg", 1: "cf", 2: "acdeg", 3: "acdfg", 4: "bcdf",
           5: "abdfg", 6: "abdefg", 7: "acf", 8: "abcdefg", 9: "abcdfg"}
nmap = {j: i for i, j in numbers.items()}
lengths = {i: len(j) for i, j in numbers.items()}
unique_lengths = {j: i for i, j in lengths.items() if list(lengths.values()).count(j) == 1}
all_lengths = {j: [k for i, k in lengths.items() if i == j] for j in lengths.values()}

out = 0
with open("input") as f:
    for line in f:
        options = {i: ["a", "b", "c", "d", "e", "f", "g"] for i in "abcdefg"}
        for digit in line.strip().split(" "):
            if digit != "|":
                for i, n in unique_lengths.items():
                    if len(digit) == i:
                        for c in digit:
                            options[c] = [j for j in options[c] if j in numbers[n]]
                        for c in "abcdefg":
                            if c not in digit:
                                options[c] = [j for j in options[c] if j not in numbers[n]]
        for digit in line.strip().split(" "):
            if digit != "|":
                valid = []
                for c in product(*[options[i] for i in digit]):
                    v = "".join(sorted(c))
                    if v in nmap and v not in valid:
                        valid.append(v)
                if len(valid) == 1:
                    for c in digit:
                        options[c] = [j for j in options[c] if j in numbers[nmap[valid[0]]]]
                    for c in "abcdefg":
                        if c not in digit:
                            options[c] = [j for j in options[c] if j not in numbers[nmap[valid[0]]]]

        for i in options.values():
            assert len(i) == 1

        N = ""
        for digit in line.split("|")[1].strip().split(" "):
            mapped = "".join(sorted([options[i][0] for i in digit]))
            N += str(nmap[mapped])
        out += int(N)
print(out)
