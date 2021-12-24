import sympy

values = {"x": 0, "y": 0, "z": 0, "w": 0}

def get_value(i):
    if i in values:
        return values[i]
    return int(i)

temp = 0
with open("f2.py", "w") as fout:
    fout.write("def f(inputs):\n")

    i = 0
    with open("input") as f:
        for line in f:
            a = line.strip().split(" ")
            if a[0] == "inp":
                values[a[1]] = sympy.Symbol(f"inputs[{i}]")
                i += 1
            elif a[0] == "add":
                values[a[1]] += get_value(a[2])
            elif a[0] == "mul":
                values[a[1]] *= get_value(a[2])
            elif a[0] == "mod":
#                if get_value(a[1]) == 0:
#                    pass
#                else:
                    fout.write(f"    {a[1]} = ({get_value(a[1])}) % ({get_value(a[2])})\n")
                    values[a[1]] = sympy.Symbol(a[1])
            elif a[0] == "div":
#                if get_value(a[1]) == 0:
#                    values[a[1]] = 0
#                elif get_value(a[2]) == 1:
#                    pass
#                else:
                    fout.write(f"    {a[1]} = ({get_value(a[1])}) // ({get_value(a[2])})\n")
                    values[a[1]] = sympy.Symbol(a[1])
            elif a[0] == "eql":
                fout.write(f"    {a[1]} = int({get_value(a[1])} == {get_value(a[2])})\n")
                values[a[1]] = sympy.Symbol(a[1])
    fout.write(f"    return {values['z']}\n")
