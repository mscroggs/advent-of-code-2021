from f import f

inputs = [None for i in range(14)]
for inputs[0] in range(9, 0, -1):
  for inputs[7] in range(9, 0, -1):
    for inputs[2] in range(3, 0, -1):
        inputs[3] = inputs[2] + 6
        for inputs[1] in range(4, 0, -1):
            inputs[4] = inputs[1] + 5
            for inputs[5] in range(8, 0, -1):
                inputs[6] = inputs[5] + 1
                for inputs[11] in range(9, 4, -1):
                    inputs[12] = inputs[11] - 4
                    for inputs[8] in range(9, 5, -1):
                        inputs[9] = inputs[8] - 5
                        for inputs[10] in range(9, 0, -1):
                            inputs[13] = inputs[10]
                            if f(inputs) == 0:
                                print("".join(str(i) for i in inputs))
                                exit()
