class Board:
    def __init__(self, b):
        self.pieces = {}
        for i, line in enumerate(b.split("\n")[1:]):
            for j, c in enumerate(line):
                if c in "ABCD":
                    self.pieces[(j, i)] = c
        self.cost = 0

    def move(self, start, end):
        assert start in self.pieces
        cost = {"A": 1, "B": 10, "C": 100, "D": 1000}[self.pieces[start]]
        p = [i for i in start]
        while p[1] > 0:
            p[1] -= 1
            assert tuple(p) not in self.pieces
            self.cost += cost
        while p[0] > end[0]:
            p[0] -= 1
            assert tuple(p) not in self.pieces
            self.cost += cost
        while p[0] < end[0]:
            p[0] += 1
            assert tuple(p) not in self.pieces
            self.cost += cost
        while p[1] < end[1]:
            p[1] += 1
            assert tuple(p) not in self.pieces
            self.cost += cost

        self.pieces[end] = self.pieces[start]
        del self.pieces[start]

        board.show()

    def show(self):
        print("            111")
        print("  0123456789012")
        print("  " + "#" * 13)
        print("0 #" + "".join([self.pieces[(i, 0)] if (i, 0) in self.pieces else "."
                             for i in range(1, 12)]) + "#")
        print("1 ###" + "#".join([self.pieces[(i, 1)] if (i, 1) in self.pieces else "."
              for i in range(3, 10, 2)]) + "###")
        print("2   #" + "#".join([self.pieces[(i, 2)] if (i, 2) in self.pieces else "."
              for i in range(3, 10, 2)]) + "#  ")
        print("3   #" + "#".join([self.pieces[(i, 3)] if (i, 3) in self.pieces else "."
              for i in range(3, 10, 2)]) + "#  ")
        print("4   #" + "#".join([self.pieces[(i, 4)] if (i, 4) in self.pieces else "."
              for i in range(3, 10, 2)]) + "#  ")
        print("5   " + "#" * 9 + "  ")
        print()

with open("input2") as f:
    board = Board(f.read())

board.move((9, 1), (1, 0))
board.move((9, 2), (2, 0))
board.move((9, 3), (11, 0))
board.move((9, 4), (10, 0))
board.move((7, 1), (9, 4))
board.move((3, 1), (9, 3))
board.move((3, 2), (9, 2))
board.move((3, 3), (9, 1))
board.move((3, 4), (8, 0))
board.move((2, 0), (3, 4))
board.move((1, 0), (3, 3))
board.move((7, 2), (2, 0))
board.move((7, 3), (3, 2))
board.move((7, 4), (3, 1))
board.move((8, 0), (7, 4))
board.move((5, 1), (4, 0))
board.move((5, 2), (7, 3))
board.move((5, 3), (8, 0))
board.move((5, 4), (7, 2))
board.move((4, 0), (5, 4))
board.move((2, 0), (5, 3))
board.move((8, 0), (5, 2))
board.move((10, 0), (5, 1))
board.move((11, 0), (7, 1))

print(board.cost)
