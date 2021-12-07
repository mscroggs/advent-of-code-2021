class Bingo:
    def __init__(self, numbers):
        numbers = numbers.strip()
        while "  " in numbers:
            numbers = numbers.replace("  ", " ")
        self.numbers = [[int(i) for i in line.strip().split(" ")] for line in numbers.split("\n")]
        self.called = [[False for i in range(5)] for j in range(5)]

    def call(self, n):
        for i, line in enumerate(self.numbers):
            for j, entry in enumerate(line):
                if n == entry:
                    self.called[i][j] = True

    def has_winner(self):
        for i in range(5):
            if len([j for j in range(5) if self.called[i][j]]) == 5:
                return True
            if len([j for j in range(5) if self.called[j][i]]) == 5:
                return True
        return False

    def sum(self):
        out = 0
        for i, line in enumerate(self.numbers):
            for j, entry in enumerate(line):
                if not self.called[i][j]:
                    out += entry
        return out

with open("input") as f:
    boards = f.read().split("\n\n")
    calls = [int(i) for i in boards[0].split(",")]
    cards = []
    for i in boards[1:]:
        cards.append(Bingo(i))

for n in calls:
    for c in cards:
        c.call(n)
    if len([c for c in cards if not c.has_winner()]) == 1:
        for c in cards:
            if not c.has_winner():
                bingo = c
                break
    if len([c for c in cards if not c.has_winner()]) == 0:
        break


print(bingo.called)

print(n * bingo.sum())
