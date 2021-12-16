with open("input") as f:
    hex = f.read().strip()

b = [0, 0, 0, -1]
hex2bin = {}
for i in "0123456789ABCDEF":
    b[-1] += 1
    n = -1
    while b[n] == 2:
        b[n] = 0
        b[n - 1] += 1
        n -= 1
    hex2bin[i] = "".join([str(j) for j in b])

bin = ""
for i in hex:
    bin += hex2bin[i]

def bin2dec(n):
    out = 0
    for i, j in enumerate(n[::-1]):
        if j == "1":
            out += 2 ** i
    return out

def get_packet(bin):
    v = bin2dec(bin[:3])
    bin = bin[3:]
    t = bin2dec(bin[:3])
    bin = bin[3:]

    if t == 4:
        packets = 0
        while bin[5*packets] == "1":
            packets += 1
        packets += 1

        n = ""
        for i in range(packets):
            n += bin[1:5]
            bin = bin[5:]
        n = bin2dec(n)
        return ("number", v, t, n), bin
    else:
        mode = bin[0]
        bin = bin[1:]
        if mode == "0":
            length = bin2dec(bin[:15])
            bin = bin[15:]
            packet = bin[:length]
            bin = bin[length:]
            subpackets = []
            while len(packet) > 0:
                p, packet = get_packet(packet)
                subpackets.append(p)
            return ("operator", v, t, subpackets), bin
        else:
            assert mode == "1"
            packets = bin2dec(bin[:11])
            bin = bin[11:]
            subpackets = []
            for i in range(packets):
                p, bin = get_packet(bin)
                subpackets.append(p)

            return ("operator", v, t, subpackets), bin

packets = []
while "1" in bin:
    p, bin = get_packet(bin)
    packets.append(p)


def get_value(packet):
    if packet[0] == "number":
        return packet[3]
    if packet[2] == 0:
        return sum(get_value(i) for i in packet[3])
    if packet[2] == 1:
        out = 1
        for i in packet[3]:
            out *= get_value(i)
        return out
    if packet[2] == 2:
        return min(get_value(i) for i in packet[3])
    if packet[2] == 3:
        return max(get_value(i) for i in packet[3])
    if packet[2] == 5:
        if get_value(packet[3][0]) > get_value(packet[3][1]):
            return 1
        else:
            return 0
    if packet[2] == 6:
        if get_value(packet[3][0]) < get_value(packet[3][1]):
            return 1
        else:
            return 0
    if packet[2] == 7:
        if get_value(packet[3][0]) == get_value(packet[3][1]):
            return 1
        else:
            return 0

assert len(packets) == 1

print(get_value(packets[0]))
