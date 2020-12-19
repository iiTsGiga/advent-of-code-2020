instructions = [line.strip().split()[::2] for line in open("day14_input.txt")]

def apply_mask(val, mask):
    v = list(bin(val)[2:].zfill(36))
    return int("".join([c if c != "X" else v[i] for i, c in enumerate(mask)]), 2)

mem = dict()
mask = ""
for i, v in instructions:
    mask = v * (i == "mask") + mask * (i != "mask")
    mem[i[4:-1]] = apply_mask(int(v), mask) if i[:3] == "mem" else 0

print(sum(mem.values()))