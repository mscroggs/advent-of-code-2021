def f(inputs):
    x = (0) % (26)
    z = (0) // (1)
    x = int(x + 12 == inputs[0])
    x = int(x == 0)
    x = (x*(inputs[0] + 15) + z*(25*x + 1)) % (26)
    z = (x*(inputs[0] + 15) + z*(25*x + 1)) // (1)
    x = int(x + 14 == inputs[1])
    x = int(x == 0)
    x = (x*(inputs[1] + 12) + z*(25*x + 1)) % (26)
    z = (x*(inputs[1] + 12) + z*(25*x + 1)) // (1)
    x = int(x + 11 == inputs[2])
    x = int(x == 0)
    x = (x*(inputs[2] + 15) + z*(25*x + 1)) % (26)
    z = (x*(inputs[2] + 15) + z*(25*x + 1)) // (26)
    x = int(x - 9 == inputs[3])
    x = int(x == 0)
    x = (x*(inputs[3] + 12) + z*(25*x + 1)) % (26)
    z = (x*(inputs[3] + 12) + z*(25*x + 1)) // (26)
    x = int(x - 7 == inputs[4])
    x = int(x == 0)
    x = (x*(inputs[4] + 15) + z*(25*x + 1)) % (26)
    z = (x*(inputs[4] + 15) + z*(25*x + 1)) // (1)
    x = int(x + 11 == inputs[5])
    x = int(x == 0)
    x = (x*(inputs[5] + 2) + z*(25*x + 1)) % (26)
    z = (x*(inputs[5] + 2) + z*(25*x + 1)) // (26)
    x = int(x - 1 == inputs[6])
    x = int(x == 0)
    x = (x*(inputs[6] + 11) + z*(25*x + 1)) % (26)
    z = (x*(inputs[6] + 11) + z*(25*x + 1)) // (26)
    x = int(x - 16 == inputs[7])
    x = int(x == 0)
    x = (x*(inputs[7] + 15) + z*(25*x + 1)) % (26)
    z = (x*(inputs[7] + 15) + z*(25*x + 1)) // (1)
    x = int(x + 11 == inputs[8])
    x = int(x == 0)
    x = (x*(inputs[8] + 10) + z*(25*x + 1)) % (26)
    z = (x*(inputs[8] + 10) + z*(25*x + 1)) // (26)
    x = int(x - 15 == inputs[9])
    x = int(x == 0)
    x = (x*(inputs[9] + 2) + z*(25*x + 1)) % (26)
    z = (x*(inputs[9] + 2) + z*(25*x + 1)) // (1)
    x = int(x + 10 == inputs[10])
    x = int(x == 0)
    x = (inputs[10]*x + z*(25*x + 1)) % (26)
    z = (inputs[10]*x + z*(25*x + 1)) // (1)
    x = int(x + 12 == inputs[11])
    x = int(x == 0)
    x = (inputs[11]*x + z*(25*x + 1)) % (26)
    z = (inputs[11]*x + z*(25*x + 1)) // (26)
    x = int(x - 4 == inputs[12])
    x = int(x == 0)
    x = (x*(inputs[12] + 15) + z*(25*x + 1)) % (26)
    z = (x*(inputs[12] + 15) + z*(25*x + 1)) // (26)
    x = int(x == inputs[13])
    x = int(x == 0)
    return x*(inputs[13] + 15) + z*(25*x + 1)
