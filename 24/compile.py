with open("f.py", "w") as fout:
    fout.write("def f(inputs):\n")
    fout.write("    w, x, y, z = 0, 0, 0, 0\n")

    i = 0
    with open("input") as f:
        for line in f:
            a = line.strip().split(" ")
            if a[0] == "inp":
                fout.write(f"    {a[1]} = inputs[{i}]\n")
                i += 1
            elif a[0] == "add":
                fout.write(f"    {a[1]} += {a[2]}\n")
            elif a[0] == "mul":
                fout.write(f"    {a[1]} *= {a[2]}\n")
            elif a[0] == "mod":
                fout.write(f"    {a[1]} %= {a[2]}\n")
            elif a[0] == "div":
                fout.write(f"    {a[1]} //= {a[2]}\n")
            elif a[0] == "eql":
                fout.write(f"    {a[1]} = int({a[1]} == {a[2]})\n")
    fout.write("    return w, x, y, z\n")
