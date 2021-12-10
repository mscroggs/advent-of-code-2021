score = 0

with open("input") as f:
    for line in f:
        line = line.strip()
        prev = ""
        while prev != line:
            prev = line
            for i in ["()", "{}", "<>", "[]"]:
                line = line.replace(i, "")
        for i in line:
            if i in ")}>]":
                if i == ")":
                    score += 3
                if i == "]":
                    score += 57
                if i == "}":
                    score += 1197
                if i == ">":
                    score += 25137
                break
print(score)
