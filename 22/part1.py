on = set()

with open("input") as f:
    for line in f:
        status, points = line.split(" ")
        points = points.split(",")
        lims = [[int(i) for i in p.split("=")[1].split("..")]
                for p in points]
        for i in range(3):
            lims[i][0] = max(-50, lims[i][0])
            lims[i][1] = min(50, lims[i][1])

        for x in range(lims[0][0], lims[0][1] + 1):
            for y in range(lims[1][0], lims[1][1] + 1):
                for z in range(lims[2][0], lims[2][1] + 1):
                    if status == "on":
                        on.add((x, y, z))
                    elif (x, y, z) in on:
                        on.remove((x, y, z))

print(len(on))
