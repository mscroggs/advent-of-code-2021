scores = []

with open("input") as f:
    for line in f:
        line = line.strip()
        start = line.strip()
        prev = ""
        while prev != line:
            prev = line
            for i in ["()", "{}", "<>", "[]"]:
                line = line.replace(i, "")
        for i in line:
            if i in ")}>]":
                break
        else:
            points = 0
            for c in line[::-1]:
                points *= 5
                if c == "(":
                    points += 1
                if c == "[":
                    points += 2
                if c == "{":
                    points += 3
                if c == "<":
                    points += 4
            print(start, line, points)
            scores.append(points)

scores.sort()
print(scores[(len(scores) - 1) // 2])

