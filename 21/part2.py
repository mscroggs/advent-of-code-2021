from itertools import product

with open("input") as f:
    positions = [int(line.split(":")[1]) for line in f]

possibles = {((0, 0), tuple(positions)): 1}
wins = [0, 0]

turn = 0
while len(possibles) > 0:
    new_possibles = {}
    for (scores, positions), n in possibles.items():
        for i in product(range(1, 4), repeat=3):
            new_s = [j for j in scores]
            new_p = [j for j in positions]
            new_p[turn] += sum(i)
            while new_p[turn] > 10:
                new_p[turn] -= 10
            new_s[turn] += new_p[turn]
            if max(new_s) >= 21:
                if new_s[0] > new_s[1]:
                    wins[0] += n
                else:
                    wins[1] += n
            else:
                key = (tuple(new_s), tuple(new_p))
                if key not in new_possibles:
                    new_possibles[key] = 0
                new_possibles[key] += n

    possibles = new_possibles
    turn = 1 - turn

print(max(wins))
