import sympy

values = {"w": 0, "x": 0, "y": 0, "z": 0}

class EqBase:
    def __rmul__(self, other):
        return MulEqual(self, other)
    def __mul__(self, other):
        return MulEqual(self, other)
    def __add__(self, other):
        return AddEqual(self, other)
    def to_python(self):
        raise NotImplementedError()
    def __str__(self):
        return self.to_python()

class MulEqual(EqBase):
    def __init__(self, mult, a):
        self.mult = mult
        self.a = a

    def to_python(self):
        return f"({self.a}) * ({self.mult.to_python()})"

class AddEqual(EqBase):
    def __init__(self, mult, a):
        self.mult = mult
        self.a = a

    def to_python(self):
        return f"({self.a}) + ({self.mult.to_python()})"

class Equal(EqBase):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def to_python(self):
        return f"int({self.a} == {self.b})"

class NotEqual(EqBase):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def to_python(self):
        return f"int({self.a} != {self.b})"

def get_value(a):
    if a in values:
        return values[a]
    return int(a)

temp = 0
def set_temp(value):
    global temp
    fout.write(f"    temp{temp} = {value}\n")
    temp += 1
    return sympy.Symbol(f"temp{temp - 1}")

with open("f4.py", "w") as fout:
    fout.write("def f(inputs):\n")
    fout.write("    w, x, y, z = 0, 0, 0, 0\n")
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
                if get_value(a[1]) == 0:
                    pass
                else:
                    values[a[1]] = set_temp(f"({get_value(a[1])}) % ({get_value(a[2])})")
            elif a[0] == "div":
                if get_value(a[1]) == 0:
                    pass
                elif get_value(a[2]) == 1:
                    pass
                else:
                    values[a[1]] = set_temp(f"({get_value(a[1])}) // ({get_value(a[2])})")
                    temp += 1
            elif a[0] == "eql":
                if isinstance(get_value(a[2]), EqBase):
                    a[1], a[2] = a[2], a[1]
                if isinstance(get_value(a[1]), EqBase) and get_value(a[2]) == 0:
                    va = values[a[1]].a
                    vb = values[a[1]].b
                    for j in range(14):
                        if vb == sympy.Symbol(f"inputs[{j}]"):
                            va, vb = vb, va
                        if va == sympy.Symbol(f"inputs[{j}]") and isinstance(vb, int) and (vb > 9 or vb < 1):
                            values[a[1]] = 1
                            break
                    else:
                        values[a[1]] = NotEqual(values[a[1]].a, values[a[1]].b)
                        values[a[1]] = set_temp(f"{get_value(a[1])}")
                else:
                    values[a[1]] = Equal(get_value(a[1]), get_value(a[2]))

    fout.write(f"    return {values['z']}\n")
