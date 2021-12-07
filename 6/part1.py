with open("input") as f:
    fish = [int(i) for i in f.read().split(",")]

for i in range(80):
    new_fish = []
    for i, j in enumerate(fish):
        if j == 0:
            fish[i] = 6
            new_fish.append(8)
        else:
            fish[i] -= 1
    fish += new_fish

print(len(fish))
