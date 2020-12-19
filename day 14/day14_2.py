instructions = [line.strip().split()[::2] for line in open("day14_input.txt")]

def get_addresses(val, mask):
    v = list(bin(val)[2:].zfill(36))
    v = [c if c != "0" else v[i] for i, c in enumerate(mask)]
    ret = []
    mods = [bin(i)[2:].zfill(v.count("X")) for i in range(pow(2, v.count("X")))]
    for mod in mods:
        i = 0
        add = ""
        for j, c in enumerate(v):
            if c != "X":
                add += c
                continue
            add += mod[i]
            i += 1
        ret.append(int(add, 2))
    return ret

mem = dict()
mask = ""
for i, v in instructions:
    mask = v * (i == "mask") + mask * (i != "mask")
    if i[:3] == "mem":
        for add in get_addresses(int(i[4:-1]), mask):
            mem[add] = int(v)

print(sum(mem.values()))
