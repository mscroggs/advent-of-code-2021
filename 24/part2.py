from f import f

inputs = [None for i in range(14)]
for inputs[0] in range(1, 10):
  for inputs[7] in range(1, 10):
    for inputs[2] in range(1, 4):
        inputs[3] = inputs[2] + 6
        for inputs[1] in range(1, 5):
            inputs[4] = inputs[1] + 5
            for inputs[5] in range(1, 9):
                inputs[6] = inputs[5] + 1
                for inputs[11] in range(5, 10):
                    inputs[12] = inputs[11] - 4
                    for inputs[8] in range(6, 10):
                        inputs[9] = inputs[8] - 5
                        for inputs[10] in range(1, 10):
                            inputs[13] = inputs[10]
                            if f(inputs) == 0:
                                print("".join(str(i) for i in inputs))
                                exit()
