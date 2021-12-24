from itertools import product
from f import f

for inputs in product(range(9, 0, -1), repeat=14):
    if sum(inputs[-5:]) == 5 * 9:
        print(inputs)
    if f(inputs) == 0:
        print("".join([str(i) for i in inputs]))
        break
