from itertools import product
from f import f
from f4 import f as f4
from random import randrange

for i in range(5000):
    inputs = [randrange(1, 10) for i in range(14)]
    assert f(inputs)[-1] == f4(inputs)
