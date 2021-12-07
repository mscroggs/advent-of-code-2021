with open("input") as f:
    fish = [int(i) for i in f.read().split(",")]

fish = {i: fish.count(i) for i in range(9)}

for i in range(256):
    new_fish = {}
    new_fish[8] = fish[0]
    new_fish[6] = fish[0] + fish[7]
    new_fish[7] = fish[8]
    for i in range(6):
        new_fish[i] = fish[i + 1]
    fish = new_fish

print(sum(fish.values()))
