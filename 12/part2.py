class Caves:
    def __init__(self):
        self.paths = {}

    def add_cave(self, cave):
        if cave not in self.paths:
            self.paths[cave] = []

    def add_path(self, cave1, cave2):
        if cave1 not in self.paths[cave2]:
            self.paths[cave2].append(cave1)
            self.paths[cave1].append(cave2)

    def find_paths(self, start=["start"]):
        if start[-1] == "end":
            return [start]
        out = []
        for i in self.paths[start[-1]]:
            if (not self.has_double(start) and i != "start") or i not in start or i.upper() == i:
                out += self.find_paths(start + [i])
        return out

    def has_double(self, start):
        for i in start:
            if i.lower() == i and start.count(i) > 1:
                return True
        return False

c = Caves()

with open("input") as f:
    for line in f:
        caves = line.strip().split("-")
        for i in caves:
            c.add_cave(i)
        for i, j in zip(caves, caves[1:]):
            c.add_path(i, j)

print(len(c.find_paths()))

