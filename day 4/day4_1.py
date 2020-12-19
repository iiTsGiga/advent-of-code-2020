print(''.join(line for line in open("day4_input.txt")).split("\n\n"))
passports = [entry.split() for entry in ''.join(line for line in open("day4_input.txt")).split("\n\n")]

valid = 0
for pp in passports:
    pp = [line[:3] for line in pp]
    valid += len(pp) == 8 or (len(pp) == 7 and "cid" not in pp)

print(valid)
